# ===================================
# Prepare Matrix / Aggregates for Visualization
# ===================================

import pandas as pd


def prepare_matrix(df):
    """
    Prepare aggregated data for dashboard visualization:
    - Total revenue by Region
    - Revenue by Product Category
    - Correlation matrix
    - Monthly sales trends
    """

    # Total revenue by Region
    revenue_by_region = df.groupby("Region")["Calculated_Revenue"].sum().reset_index()

    # Revenue by Category
    revenue_by_category = (
        df.groupby("Category")["Calculated_Revenue"].sum().reset_index()
    )

    # Correlation matrix
    corr_matrix = df[["Quantity", "Discount", "Calculated_Revenue"]].corr()

    # Monthly sales trends
    monthly_revenue = (
        df.groupby(["Year", "Month_Name"])["Calculated_Revenue"].sum().reset_index()
    )

    # Sort months correctly
    months_order = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    monthly_revenue["Month_Name"] = pd.Categorical(
        monthly_revenue["Month_Name"], categories=months_order, ordered=True
    )
    monthly_revenue = monthly_revenue.sort_values(["Year", "Month_Name"])

    return revenue_by_region, revenue_by_category, corr_matrix, monthly_revenue


# -----------------------------
# Execute when run directly
# -----------------------------
if __name__ == "__main__":
    df = pd.read_csv(
        "../data/processed/fact_sales_features.csv", parse_dates=["Date", "Signup_Date"]
    )
    region_matrix, category_matrix, corr_matrix, monthly_matrix = prepare_matrix(df)
    print("Matrices prepared successfully.")
