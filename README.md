# 📊 Marketing Funnel & Conversion Performance Analysis
### Future Intern — Data Science & Analytics Internship | Task 3

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat&logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c?style=flat)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4c8cbf?style=flat)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?style=flat&logo=jupyter)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)
![Internship](https://img.shields.io/badge/Future%20Intern-Task%203-blueviolet?style=flat)

---

## 📌 Project Overview

This project is the **third task** of the **Future Intern Data Science & Analytics Internship**.
It performs a complete **Exploratory Data Analysis (EDA)** on a custom Marketing Funnel dataset
to uncover actionable insights about campaign performance, conversion rates, ROI, and customer
behaviour across all stages of the marketing funnel.

---

## 📁 Project Structure
```
Marketing-Funnel-Conversion-Analysis/
│
├── EDA_marketing_funnel.ipynb          # Main Jupyter Notebook (Full EDA)
├── Marketing_Funnel_Dataset.csv        # Source dataset (custom — 1,000 records)
├── marketing_funnel_results.csv        # Exported analysis summary results
└── README.md                           # Project documentation
```

---

## 📂 Dataset Description

**File:** `Marketing_Funnel_Dataset.csv` — Custom Dataset  
**Total Records:** 1,000 | **Time Period:** January 2024 – December 2024

| Column | Data Type | Description |
|--------|-----------|-------------|
| Customer_ID | String | Unique customer identifier |
| Campaign_Name | String | Email Campaign, Social Media, PPC Ads, SEO, Referral Program |
| Campaign_Channel | String | Facebook, Google, Email, Instagram, YouTube |
| Funnel_Stage | String | Awareness / Interest / Consideration / Intent / Conversion |
| Date | Date | Date the interaction occurred |
| Impressions | Integer | Number of times the ad was shown |
| Clicks | Integer | Number of clicks on the ad/campaign |
| Website_Visits | Integer | Number of visits to the website |
| Leads_Generated | Integer | Number of potential customers captured |
| Sign_Ups | Integer | Number of users who signed up |
| Add_To_Cart | Integer | Number of users who added product to cart |
| Purchases | Integer | Number of completed purchases |
| Revenue | Float | Revenue generated from purchases ($) |
| Ad_Spend | Float | Amount spent on the campaign ($) |
| Cost_Per_Click | Float | Ad spend divided by clicks |
| Conversion_Rate | Float | Purchases / Clicks × 100 |
| ROI | Float | (Revenue − Ad Spend) / Ad Spend × 100 |
| Customer_Segment | String | New / Returning / Premium |
| Device | String | Mobile / Desktop / Tablet |
| Region | String | North / South / East / West |

---

## 📊 Key Findings

| Metric | Value |
|--------|-------|
| 💰 Total Revenue | $2,840,000 |
| 💸 Total Ad Spend | $2,550,000 |
| 📈 Overall ROI | 391% |
| 🎯 Avg Conversion Rate | 1.07% |
| 👆 Total Clicks | 1,980,000 |
| 🏆 Best Channel (ROI) | Email |
| 📣 Best Campaign (Revenue) | Email Campaign |
| 👥 Best Customer Segment | Premium |
| 📱 Top Device | Mobile |
| 🌍 Best Region | North |

---

## 🔍 Analysis Performed

1. **Funnel Stage Analysis** — Customer count per stage, drop-off rates, and stage-wise conversion metrics
2. **Conversion Rate Analysis** — Overall, by channel, by campaign, and by customer segment
3. **ROI & Ad Spend Analysis** — Total financials, ROAS, net profit per channel
4. **Channel Performance Analysis** — Impressions, CTR, CPC, conversion rate, and ROAS by channel
5. **Campaign Performance Analysis** — Revenue vs ad spend comparison across all 5 campaigns
6. **Customer Segment Analysis** — Revenue, conversion rate, and ROI for New, Returning, and Premium segments
7. **Device & Region Analysis** — Revenue share by device type and regional performance breakdown
8. **Time Series / Monthly Trend Analysis** — Monthly revenue, ad spend, and conversion rate trends
9. **Scatter Analysis** — Ad spend vs revenue correlation by channel
10. **Correlation Heatmap** — Relationships between all numeric features

---

## 📈 Visualisations

| Chart | Type | Insight |
|-------|------|---------|
| Funnel Stage Drop-off | Bar Chart | Where customers are lost in the funnel |
| Conversion Rate by Channel | Bar Chart | Which channel converts best |
| ROI by Campaign | Horizontal Bar | Most cost-efficient campaigns |
| Monthly Revenue Trend | Line Chart | Seasonality and growth patterns |
| Ad Spend vs Revenue | Scatter Plot | Spending efficiency per channel |
| Revenue by Device | Donut Chart | Which device drives most revenue |
| Revenue by Segment | Donut Chart | Segment contribution to total revenue |
| Channel Performance | Grouped Bar | Full metrics dashboard per channel |
| Correlation Heatmap | Heatmap | Feature relationships and dependencies |

---

## 🛠️ Technologies Used

| Tool | Purpose |
|------|---------|
| **Python 3.x** | Core programming language |
| **Pandas** | Data manipulation and analysis |
| **NumPy** | Numerical computations |
| **Matplotlib** | Static data visualisation |
| **Seaborn** | Statistical plots and styling |
| **Jupyter Notebook** | Interactive development environment |

---

## 💡 Business Insights Summary

- **Email** channel delivers the highest ROI — the most cost-efficient marketing channel
- The **Awareness → Interest** stage has the highest drop-off — mid-funnel content needs improvement
- **Premium** customers generate the most revenue despite lower volume — a key retention target
- **Mobile** devices dominate revenue share — all campaigns should be mobile-optimised
- **Q4** (Oct–Dec) shows the strongest conversion rates — ideal time to scale ad budgets

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🙌 Acknowledgements

- **Future Intern** — For providing this Data Science & Analytics internship opportunity
- The dataset (`Marketing_Funnel_Dataset.csv`) is an original custom dataset created specifically for this project

---

> ⭐ If you found this project helpful, consider giving it a star on GitHub!
