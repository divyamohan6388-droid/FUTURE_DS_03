import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(42)
n = 1000
campaigns = ['Email Campaign', 'Social Media', 'PPC Ads', 'SEO', 'Referral Program']
channels = ['Facebook', 'Google', 'Email', 'Instagram', 'YouTube']
stages = ['Awareness', 'Interest', 'Consideration', 'Intent', 'Conversion']
segments = ['New', 'Returning', 'Premium']
devices = ['Mobile', 'Desktop', 'Tablet']
regions = ['North', 'South', 'East', 'West']

start = datetime(2024, 1, 1)
dates = [start + timedelta(days=random.randint(0, 364)) for _ in range(n)]
impressions = np.random.randint(500, 50000, n)
clicks = (impressions * np.random.uniform(0.01, 0.15, n)).astype(int)
website_visits = (clicks * np.random.uniform(0.5, 0.9, n)).astype(int)
leads = (website_visits * np.random.uniform(0.1, 0.4, n)).astype(int)
signups = (leads * np.random.uniform(0.2, 0.6, n)).astype(int)
add_to_cart = (signups * np.random.uniform(0.3, 0.7, n)).astype(int)
purchases = (add_to_cart * np.random.uniform(0.2, 0.5, n)).astype(int)
revenue = purchases * np.random.uniform(50, 500, n)
ad_spend = np.random.uniform(100, 5000, n)
cpc = np.where(clicks > 0, ad_spend / clicks, 0).round(2)
conv_rate = np.where(clicks > 0, purchases / clicks * 100, 0).round(2)
roi = ((revenue - ad_spend) / ad_spend * 100).round(2)

df = pd.DataFrame({
'Customer_ID' : [f'CUST{i+1000}' for i in range(n)],
'Campaign_Name' : np.random.choice(campaigns, n),
'Campaign_Channel' : np.random.choice(channels, n),
'Funnel_Stage' : np.random.choice(stages, n),
'Date' : [d.strftime('%d-%m-%Y') for d in dates],
'Impressions' : impressions,
'Clicks' : clicks,
'Website_Visits' : website_visits,
'Leads_Generated' : leads,
'Sign_Ups' : signups,
'Add_To_Cart' : add_to_cart,
'Purchases' : purchases,
'Revenue' : revenue.round(2),
'Ad_Spend' : ad_spend.round(2),
'Cost_Per_Click' : cpc,
'Conversion_Rate' : conv_rate,
'ROI' : roi,
'Customer_Segment' : np.random.choice(segments, n),
'Device' : np.random.choice(devices, n),
'Region' : np.random.choice(regions, n),
})

df.to_csv('Marketing_Funnel_Dataset.csv', index=False)
print(f"Dataset created: {df.shape[0]} rows x {df.shape[1]} columns")
print(df.head())