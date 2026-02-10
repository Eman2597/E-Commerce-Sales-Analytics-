# 📊 E-Commerce Sales Intelligence Dashboard

**An End-to-End Data Engineering & Business Analytics Project**

![E-Commerce Dashboard](Dashboard.png)

---

## 🌟 Project Overview
This project transforms fragmented e-commerce transaction data into a **Strategic Dashboard**.  
The goal: build a robust data pipeline for **data cleaning, merging multiple sources**, and **visualizing key business metrics** to drive **data-informed decision-making**.

---

## 📖 Data Journey: From Chaos to Insights

### 1. Data Cleaning & Wrangling
- **Transaction Issues:** Fixed missing `CustomerID` and inconsistent pricing formats.  
- **Data Integrity:** Removed duplicates and validated numerical fields.  
- **Outliers:** Managed extreme revenue values for accurate analysis.  

### 2. Engineering the "Single Source of Truth"
- **Data Consolidation:** Joined Sales, Products, and Customer tables into `fact_sales_features.csv`.  
- **Feature Engineering:** Created new time-based features (`Month_Year`, `Day_Date`) and calculated fields (`Total_Amount`) for analysis.  

### 3. Metric Aggregation
- **Revenue Growth:** Month-over-month performance.  
- **Regional Concentration:** High-performing geographical zones.  
- **Correlation Matrix:** Relationships between price, quantity, and total sales.  

---

## 📈 Dashboard Insights & Recommendations

### Geographical Dominance
- **Insight:** North region drives most revenue.  
- **Recommendation:** Focus inventory and marketing campaigns there.  

### Category Variability
- **Insight:** Furniture & Clothing have high revenue variance; Electronics is stable.  
- **Recommendation:** Upsell Furniture to leverage high-value transactions.  

### Sales Anomalies
- **Insight:** Sharp decline in sales detected early 2023.  
- **Recommendation:** Investigate external factors or data gaps.  

---

## 🛠️ Technical Details
- **Libraries:** `pandas` (ETL), `seaborn` (visualization), `matplotlib` (layout).  
- **Processing:**  
  - Date parsing for accurate time-series plotting.  
  - Log scaling for Boxplots with extreme price ranges.  
- **Dashboard Layout (2x2 Grid):**  
  - Bar Plot: Regional revenue totals  
  - Box Plot: Category distribution & outliers  
  - Line Plot: Monthly sales trends  
  - Heatmap: Feature correlation matrix  

---

## 🚀 Future Roadmap
- **Predictive Analytics:** Forecast future sales.  
- **Customer Segmentation:** RFM analysis for "Champion" customers.  
- **Automated Reporting:** Monthly PDF dashboard generation.  

---

## 📁 How to Run
1. Ensure Python is installed.  
2. Install dependencies:
```bash
pip install pandas seaborn matplotlib
