# 🛒 Customer Segmentation, Churn Prediction, and Forecasting with Online Retail II Dataset

👤 ***Author:*** Daniel Kimeu  
📅 ***Date:*** 2025  

## 🚀 How to Run the Streamlit App

Follow the steps below to run the dashboard locally:

### 1. 📦 Install dependencies

Create a virtual environment and install the required packages:

```bash
# Optional: create and activate a virtual environment
python -m venv myvenv
source myvenv/Scripts/activate    # On Windows
# Or: 
source myvenv/bin/activate  # On macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

## project structure
```
DATA_ANALYTICS/
│
├── Online_Retail/
│   ├── online_retail_II.csv           # Original raw dataset
│   ├── cleaned_online_retail.csv      # Cleaned version used by the app
│   ├── customer_segments.csv          # RFM + churn features
│   └── images/                        # images used
│
├── online_retail.ipynb                # Notebook to clean & transform data
├── streamlit_app.py                   # Streamlit dashboard
├── requirements.txt                   # All required packages
└── README.md
```

## 📌 Project Overview
This project analyzes the **Online Retail II dataset** (from [Kaggle](https://www.kaggle.com/datasets)) — a real-world e-commerce dataset containing ~500K transactions from 2009–2010.  
The goal is to explore customer purchasing behavior, segment customers for targeted marketing, and identify churn risks to improve retention strategies.

---
## 📖 Introduction

Understanding customer behavior is the cornerstone of any successful retail business.  
This project leverages the **Online Retail II dataset** (500K+ transactions from a UK-based online store between 2009–2010) to explore:

- **Customer Segmentation** using RFM analysis and KMeans clustering  
- **Churn Analysis** to identify at-risk groups and retention opportunities  
- **Sales Forecasting** with Facebook Prophet for predictive business planning  

By combining **data science techniques** with **business insights**, this project transforms raw transactional data into actionable strategies that can improve customer retention, optimize marketing spend, and guide revenue growth.


## ⚙️ Tools & Technologies
- **Python**: pandas, numpy, scikit-learn  
- **Visualization**: matplotlib, seaborn  
- **Segmentation**: RFM Analysis (Recency, Frequency, Monetary)  
- **Clustering**: KMeans  
- **Churn Analysis**: Time-based cutoff method  
- **Interactive App**: Streamlit (planned deployment)  

---

## 🔍 Key Insights
- **Top Customers:** A small group of Champions drive a disproportionate share of revenue.  
- **Customer Segmentation (RFM):**
  - **Champions & Loyal Customers:** 0% churn, strong retention.  
  - **At Risk & Hibernating:** >80% churn, need targeted re-engagement.  
  - **Potential Loyalists:** A growing group that can be nurtured into Champions.  
- **Churn Analysis:**
  - Overall churn ≈ 20–25%, but concentrated in “At Risk” and “Hibernating”.  
  - ML-based clustering highlighted one group (Cluster 1) with **100% churn**.  

---

## 📊 Business Recommendations
- **Reward Champions**: VIP access, exclusive promotions, and loyalty programs.  
- **Nurture Potential Loyalists**: Personalized offers and education campaigns.  
- **Recover At Risk Customers**: Targeted win-back campaigns (discounts, reminders).  
- **Limit Spend on Hibernating**: Only seasonal or low-cost campaigns.  
- **Validate Strategies with Clusters**: Use clustering alongside RFM to detect hidden at-risk groups.  

---

## 📊 Interactive Dashboard (Streamlit)

To make the analysis accessible and interactive, I built a **Streamlit dashboard** with the following features:

- 🔎 **Filters**: Date range, country, customer segment  
- 💰 **KPIs**: Total sales, total customers, average order value, churn rate  
- 📈 **Overview Tab**: Monthly sales trends, top products, top countries  
- 👥 **Segmentation Tab**: RFM segments and KMeans clusters distribution  
- ⚠️ **Churn Analysis Tab**: Churn rates by segment and cluster  


### Dashboard Preview
- Dashboard Overview

![Dashboard Overview](/Online_Retail/images/dashboard_overview.png)  

- Segmentation Tab

![Segmentation Tab](/Online_Retail/images/segmentation.png)
- Churn Analysis Tab  

![Churn Analysis Tab](/Online_Retail/images/churn_analysis.png)  

### Run the Dashboard Locally
```bash
streamlit run streamlit_app.py
```

### 🔮 Forecasting Tab
- Uses **Facebook Prophet** to forecast sales for the next 6 months.  
- Provides confidence intervals for business planning.  

![Churn Analysis Tab](/Online_Retail/images/sales_forecast.png) 

## 🏁 Conclusion

This project demonstrates how advanced analytics can turn raw e-commerce data into **strategic business insights**:

- Identified **Champions and Loyal Customers** who should be rewarded and retained.  
- Highlighted **At Risk and Hibernating customers** with high churn rates, enabling targeted win-back campaigns.  
- Validated findings through both **rule-based RFM segmentation** and **machine learning clustering**, ensuring robustness.  
- Extended analysis into the future with a **6-month sales forecast**, giving decision-makers a forward-looking view.  

📊 **Business Value:**  
By applying these insights, companies can **increase retention, allocate marketing resources more effectively, and improve long-term revenue growth**.

🚀 **Future Work:**  
- Deploy the dashboard online (e.g., Streamlit Cloud / Hugging Face Spaces)  
- Add a recommendation system (next-best product/customer targeting)  
- Automate ETL pipelines for real-time insights  
