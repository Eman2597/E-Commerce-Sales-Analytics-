import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Set visual theme for professional looking plots
sns.set_theme(style="whitegrid")

# 2. Load and prepare data
try:
    # Load dataset with date parsing
    df = pd.read_csv("../data/processed/fact_sales_features.csv", parse_dates=["Date"])
    # Create Year-Month column for time series analysis
    df["Month_Year"] = df["Date"].dt.to_period("M").astype(str)
except Exception as e:
    print(f"Error loading data: {e}")
    exit()

# 3. Calculate Key Performance Indicators (KPIs)
total_revenue = df["Calculated_Revenue"].sum()
total_orders = len(df)
Quantity_sold = df["Quantity"].sum()
avg_order_value = total_revenue / total_orders
unique_customers = df["CustomerID"].nunique()

# 4. Prepare data for the 4 plots
region_data = (
    df.groupby("Region")["Calculated_Revenue"]
    .sum()
    .reset_index()
    .sort_values("Calculated_Revenue", ascending=False)
)
monthly_trend = df.groupby("Month_Year")["Calculated_Revenue"].sum().reset_index()

# Prepare Correlation Matrix for the Heatmap (Using only numerical columns)
corr_matrix = df.select_dtypes(include=["number"]).corr()

# 5. Create Dashboard Layout (2x2 Grid)
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(16, 12))

# --- Add KPI Header at the top ---
kpi_text = (
    f"Total Revenue: ${total_revenue:,.0f}  |  Total Orders: {total_orders:,}  |  "
    f"AOV: ${avg_order_value:,.2f} |  Customers: {unique_customers:,} |  Quantity Sold: {Quantity_sold:,}"
)
fig.suptitle(kpi_text, fontsize=20, fontweight="bold", color="#2c3e50", y=0.98)

# --- Plot 1: Revenue by Region (Bar Chart) ---
sns.barplot(
    data=region_data,
    x="Region",
    y="Calculated_Revenue",
    ax=axes[0, 0],
    palette="viridis",
)
axes[0, 0].set_title("Total Revenue by Region", fontsize=14, fontweight="bold")

# --- Plot 2: Revenue Distribution (Boxplot) ---
sns.boxplot(
    data=df, x="Category", y="Calculated_Revenue", ax=axes[0, 1], palette="Set2"
)
axes[0, 1].set_title(
    "Revenue Distribution per Category", fontsize=14, fontweight="bold"
)
axes[0, 1].set_yscale("log")

# --- Plot 3: Monthly Revenue Trend (Line Chart) ---
sns.lineplot(
    data=monthly_trend,
    x="Month_Year",
    y="Calculated_Revenue",
    ax=axes[1, 0],
    marker="o",
    color="#e74c3c",
    linewidth=2,
)
axes[1, 0].set_title("Monthly Sales Growth", fontsize=14, fontweight="bold")
axes[1, 0].tick_params(axis="x", rotation=45)

# --- Plot 4: Feature Correlation (Heatmap) ---
sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="RdBu",
    center=0,
    ax=axes[1, 1],
    fmt=".2f",
    linewidths=0.5,
)
axes[1, 1].set_title("Feature Correlation Matrix", fontsize=14, fontweight="bold")

# 6. Final Layout Adjustments
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# 7. Show the final Dashboard
plt.show()
