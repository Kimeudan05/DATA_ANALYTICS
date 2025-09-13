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
├── assets/
│   ├── online_retail_II.csv           # Original raw dataset (2009 - 2010)
|   ├── Online_Retail.csv              # Original raw dataset(2010 - 2011)
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
This project analyzes the **Online Retail dataset**  
and **Online Retail II dataset**
(from [Kaggle](https://www.kaggle.com/datasets/ulrikthygepedersen/online-retail-dataset)) — real-world e-commerce datasets containing more that 800k transactions transactions from 2009–2011. 
I have downloaded them and added them to my project folder 
 - [Online_Retail.csv](Online_Retail\Online_Retail.csv) - containing 541909 rows
- [online_retail_II.csv](Online_Retail\online_retail_II.csv) - containing around 525461  rows

The goal is to explore customer purchasing behavior, segment customers for targeted marketing, and identify churn risks to improve retention strategies.

---
## 📖 Introduction

Understanding customer behavior is the cornerstone of any successful retail business.  
This project leverages a joined dataset **Online Retail datasets** (700+ transactions from a UK-based online store between 2009–2011) to explore:

- **Customer Segmentation** using RFM analysis and KMeans clustering  
- **Churn Analysis** to identify at-risk groups and retention opportunities  
- **Sales Forecasting** with Facebook Prophet for predictive business planning  

By combining **data science techniques** with **business insights**, this project transforms raw transactional data into actionable strategies that can improve customer retention, optimize marketing spend, and guide revenue growth.


## ⚙️ Tools & Technologies
- **Python**: pandas, numpy, scikit-learn  
- **Visualization**: matplotlib, seaborn, plotly
- **Segmentation**: RFM Analysis (Recency, Frequency, Monetary)  
- **Clustering**: KMeans  
- **Churn Analysis**: Time-based cutoff method  
- **Interactive App**: Streamlit for deployment 

---

## 🔍 Key Insights
| Segment             | RFM Characteristics               | Business Action                                                                 |
|---------------------|-----------------------------------|----------------------------------------------------------------------------------|
| **Champions**       | R=4–5, F=4–5, M=4–5               | Reward loyalty, early access to new products, VIP programs                      |
| **Loyal Customers** | R=3–5, F=3–5, M=2–4               | Keep engaged with personalized offers, upsell higher-value items                |
| **Potential Loyalists** | R=3–4, F=2–3, M=2–3           | Nurture with targeted campaigns, encourage repeat purchases                     |
| **Recent Customers**| R=4–5, F=1–2, M=1–2               | Welcome campaigns, onboarding offers                                            |
| **Promising**       | R=3–4, F=1–2, M=1–2               | Educate them with product recommendations                                       |
| **At Risk**         | R=1–2, F=2–3, M=2–3               | Win-back campaigns, discounts, reminders                                        |
| **Hibernating**     | R=1–2, F=1–2, M=1–2               | Re-engagement campaigns, seasonal promos                                        |
| **Other**            | R=1, F=1, M=1                     | Consider dropping from campaigns or only send high-discount offers             |
- **Top Customers:** A small group of Champions drive a disproportionate share of revenue.  
- **Customer Segmentation (RFM):**
  - **Champions & Loyal Customers:** 0% churn, strong retention.  
  - **At Risk & Hibernating:** >100% churn, need targeted re-engagement.  
  - **Potential Loyalists:** A growing group that can be nurtured into Champions.  
- **Churn Analysis:**
  - Overall churn ≈ 40.83%, but concentrated in “At Risk” and “Hibernating”.  
  - ML-based clustering highlighted one group (Cluster 0) with **100% churn**.  

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

![Dashboard Overview](/assets/images/dashboard_overview.png)  

- Segmentation Tab

![Segmentation Tab](/assets/images/segmentation.png)
- Churn Analysis Tab  

![Churn Analysis Tab](/assets/images/churn_analysis.png)  

### Run the Dashboard Locally
```bash
streamlit run streamlit_app.py
```

### 🔮 Forecasting Tab
- Uses **Facebook Prophet** to forecast sales for the next 6 months.  
- Provides confidence intervals for business planning.  

![Churn Analysis Tab](assets/images/sales_forecast.png.png)
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
