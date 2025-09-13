import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from prophet import Prophet
import plotly.express as px

#load data
@st.cache_data
def load_data():
    df= pd.read_csv("cleaned_online_retail.csv",parse_dates=['InvoiceDate'])
    return df

df= load_data()
px.defaults.template = "plotly_dark"


# sidebar filters
st.sidebar.header("Filters")

#date range
min_date,max_date = df['InvoiceDate'].min(),df['InvoiceDate'].max()
date_range = st.sidebar.date_input("Select Date Range", [min_date, max_date])

if len(date_range) == 2:
    start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
    df = df[(df['InvoiceDate'] >= start_date) & (df['InvoiceDate'] <= end_date)]
# Else: do nothing — keep full date range
#country filter
countries = df['Country'].unique()
selected_country = st.sidebar.multiselect("Select Countries", countries, default=list(countries))

if selected_country:
    df = df[df['Country'].isin(selected_country)]
# Else: do nothing (show all countries)

st.title("Online Retail II dashboard")

#KPIs

total_sales = df['TotalAmount'].sum()
total_customers = df['CustomerId'].nunique()
avg_order_value = df.groupby('InvoiceNo')['TotalAmount'].sum().mean()

col1,col2,col3 = st.columns(3)

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Sales", f"${total_sales:,.0f}")
col2.metric("👥 Customers", f"{total_customers:,}")
col3.metric("🛍️ Avg Order Value", f"${avg_order_value:,.2f}")


# Tabs
tab1,tab2,tab3,tab4 = st.tabs(["📈 Overview", "👥 Segmentation", "⚠️ Churn Analysis", "🔮 Forecasting"])

# Overview Tab
with tab1:
    st.subheader("Monthly Sales Trend")
    monthly_sales = df.groupby(df['InvoiceDate'].dt.to_period('M'))['TotalAmount'].sum().reset_index()
    monthly_sales['InvoiceDate'] = monthly_sales['InvoiceDate'].dt.to_timestamp()

    if not monthly_sales.empty:
        fig = px.line(monthly_sales, x='InvoiceDate', y='TotalAmount',
                      markers=True,
                      labels={'InvoiceDate': 'Date', 'TotalAmount': 'Sales (€)'},
                      title='Monthly Sales Trend')
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No data available for the selected filters.")

    
    st.subheader("Top 10 Products")
    top_products = df.groupby("Description")['Quantity'].sum().nlargest(10).reset_index()

    fig = px.bar(top_products, x='Quantity', y='Description', orientation='h',
                 labels={'Quantity': 'Quantity Sold', 'Description': 'Product'},
                 title='Top 10 Products')
    fig.update_layout(height=500, yaxis=dict(autorange="reversed"))
    st.plotly_chart(fig, use_container_width=True)



    st.subheader("Top Countries by Revenue")
    country_sales = df.groupby("Country")['TotalAmount'].sum().nlargest(10).reset_index()

    fig = px.bar(country_sales, x='TotalAmount', y='Country', orientation='h',
                 labels={'TotalAmount': 'Revenue (€)', 'Country': 'Country'},
                 title='Top Countries by Revenue')
    fig.update_layout(height=500, yaxis=dict(autorange="reversed"))
    st.plotly_chart(fig, use_container_width=True)

# segmentation Tab


with tab2:
    st.subheader("Customer segmentation (RFM)")
    rfm = pd.read_csv('customer_segments.csv')

    # Segment counts sorted
    segment_counts = rfm['Segment'].value_counts().sort_values(ascending=False).reset_index()
    segment_counts.columns = ['Segment', 'Count']

    fig1 = px.bar(segment_counts, x='Segment', y='Count',
                  title="Customer Segments (Sorted)",
                  labels={'Count': 'Number of Customers'},
                  text='Count')
    fig1.update_layout(xaxis={'categoryorder':'total descending'})
    fig1.update_traces(marker_color='#1f77b4')  # light blue like st.bar_chart
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader('Cluster distribution')
    cluster_counts = rfm['Cluster'].value_counts().sort_values(ascending=False).reset_index()
    cluster_counts.columns = ['Cluster', 'Count']

    fig2 = px.bar(cluster_counts, x='Cluster', y='Count',
                  title="Cluster Distribution",
                  labels={'Count': 'Number of Customers'},
                  text='Count')
    fig2.update_layout(xaxis={'categoryorder':'total descending'})
    fig2.update_traces(marker_color='#1f77b4')  # light blue like st.bar_chart
    st.plotly_chart(fig2, use_container_width=True)

       
# churn tab
with tab3:
    st.subheader("Churn Rate By segment")
    churn_by_segment = rfm.groupby('Segment')['Churned'].mean()
    st.bar_chart(churn_by_segment)
    
    st.subheader("Churn Rate by Cluster")
    churn_by_cluster = rfm.groupby('Cluster')['Churned'].mean() *100
   
    st.bar_chart(churn_by_cluster)
    
    st.write("Exact Churn Rates (in %):")
    st.dataframe(churn_by_cluster.round(2))
    
import plotly.graph_objects as go

with tab4:
    st.subheader("Sales Forecast (Next 6 Months)")

    monthly_sales = df.groupby(df['InvoiceDate'].dt.to_period('M'))['TotalAmount'].sum().reset_index()
    monthly_sales['InvoiceDate'] = monthly_sales['InvoiceDate'].dt.to_timestamp()
    sales = monthly_sales.rename(columns={'InvoiceDate':'ds','TotalAmount':'y'})

    st.write("Sales Data Sample:")
    st.write(sales.head())

    try:
        model = Prophet()
        model.fit(sales)

        future = model.make_future_dataframe(periods=6, freq='MS')
        forecast = model.predict(future)

        st.write("Forecast Sample:")
        st.write(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].head())

        # Create plotly figure
        fig = go.Figure()

        # Historical data
        fig.add_trace(go.Scatter(
            x=sales['ds'],
            y=sales['y'],
            mode='markers+lines',
            name='Historical Sales',
            line=dict(color='blue'),
            marker=dict(size=6)
        ))

        # Forecast yhat line
        fig.add_trace(go.Scatter(
            x=forecast['ds'],
            y=forecast['yhat'],
            mode='lines',
            name='Forecast',
            line=dict(color='orange')
        ))

        # Upper confidence bound
        fig.add_trace(go.Scatter(
            x=forecast['ds'],
            y=forecast['yhat_upper'],
            mode='lines',
            name='Upper Confidence',
            line=dict(width=0),
            showlegend=False
        ))

        # Lower confidence bound, fill between with upper bound
        fig.add_trace(go.Scatter(
            x=forecast['ds'],
            y=forecast['yhat_lower'],
            mode='lines',
            fill='tonexty',
            fillcolor='rgba(255, 165, 0, 0.2)',  # translucent orange
            name='Confidence Interval',
            line=dict(width=0),
        ))

        fig.update_layout(
            title='Monthly Sales Forecast (Interactive)',
            xaxis_title='Date',
            yaxis_title='Sales (£)',
            template='plotly_dark',
            hovermode='x unified'
        )

        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"Error in forecasting: {e}")
