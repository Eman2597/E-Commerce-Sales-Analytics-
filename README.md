📊 E-Commerce Sales Intelligence Dashboard
An End-to-End Data Engineering & Business Analytics Project
🌟 Project Overview
This project transforms fragmented, raw e-commerce transaction data into a high-level Strategic Dashboard. The goal was to build a robust data pipeline that handles data cleaning, merging multiple sources, and visualizing key business metrics to drive data-informed decision-making.
📖 The Data Journey: From Chaos to Insights
1. Data Cleaning & Wrangling (The Foundation)
The project started with raw transaction logs that contained several challenges:
Transaction Table Issues: Fixed missing values in CustomerID and corrected inconsistent pricing formats.
Data Integrity: Handled duplicates and ensured that all numerical fields were valid for mathematical operations.
Outlier Management: Identified and treated extreme values in revenue to ensure the analysis represents the true business core.
2. Engineering the "Single Source of Truth"
After cleaning, I performed a complex Table Merge operation:
Data Consolidation: Joined Sales, Products, and Customer tables to create fact_sales_features.csv.
Feature Engineering: Derived new time-based features (Month_Year, Day_Date) and calculated fields (Total_Amount) to enable advanced time-series analysis.
3. Metric Aggregation
Calculated critical Business KPIs using Python's grouping logic:
Revenue Growth: Measured month-over-month performance.
Regional Concentration: Identified high-performing geographical zones.
Correlation Matrix: Analyzed the relationship between price, quantity, and total sales.
📈 Dashboard Insights & Business Findings
1. Geographical Dominance
Insight: The North region is the primary revenue driver, significantly outperforming all other regions.
Recommendation: Focus inventory and premium marketing campaigns on the North region to maximize ROI.
2. Category Variability
Insight: Furniture and Clothing show high revenue variance with several high-value outliers. Electronics remains the most stable category.
Recommendation: Implement upselling strategies for Furniture to capitalize on those high-value transactions.
3. Sales Anomalies
Insight: A sharp decline in sales was detected in the monthly trend analysis starting early 2023.
Recommendation: Urgent investigation into external factors or data collection gaps during that period is required.
🛠️ Technical Documentation
Core Implementation Logic
Library Stack: Pandas (ETL), Seaborn (Statistical Visualization), Matplotlib (Layout Management).
Processing Pipeline:
Date Parsing: Converted strings to datetime objects for accurate time-series plotting.
Log Scaling: Applied to the Boxplot (set_yscale('log')) to effectively visualize categories with extreme price ranges.
Dashboard Architecture: A modular 2x2 Grid Layout designed for scannability:
Bar Plot: Regional Revenue totals.
Box Plot: Distribution and Outliers per category.
Line Plot: Monthly sales growth trends.
Heatmap: Statistical correlation matrix between features.
🚀 Future Roadmap
Predictive Analytics: Implementing a machine learning model to predict future sales trends.
Customer Segmentation: Adding RFM (Recency, Frequency, Monetary) analysis to identify "Champion" customers.
Automated Reporting: Setting up a script to auto-generate this dashboard as a PDF report monthly.
📁 How to Run
Ensure you have Python installed.
Install dependencies: pip install pandas seaborn matplotlib.
Place your data in ../data/processed/fact_sales_features.csv.
Run the script: python dashboard.py.
