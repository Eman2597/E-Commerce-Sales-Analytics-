# ===================================
# Script for Feature Engineering
# ===================================

import pandas as pd


# -----------------------------
# 1️⃣ Feature Engineering on Fact Table
# -----------------------------
def feature_engineering(
    file_path="../data/processed/fact_sales_merged.csv",
    output_path="../data/processed/fact_sales_features.csv",
):
    """
    Load merged fact table, create new features for analysis,
    and save the final table with features.
    """
    # Load merged table
    df = pd.read_csv(file_path)

    # -----------------------------
    # Ensure Date column is datetime
    # -----------------------------
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Forward fill missing dates if any
    df["Date"] = df["Date"].ffill()

    # -----------------------------
    # Calculated Revenue
    # -----------------------------
    df["Calculated_Revenue"] = df["Quantity"] * df["Price"] * (1 - df["Discount"])

    # Optional: Difference between dirty Total_Amount and Calculated Revenue
    df["Difference"] = df["Calculated_Revenue"] - df["Total_Amount"]

    # -----------------------------
    # Time Features
    # -----------------------------
    df["Month"] = df["Date"].dt.to_period("M").astype(str)
    # Create a new column with month names
    df["Month_Name"] = df["Date"].dt.month_name()

    # Optional: also keep year if needed
    df["Year"] = df["Date"].dt.year

    # Preview
    df[["Date", "Month_Name", "Year"]].head(10)

    # -----------------------------
    # Save the feature table
    # -----------------------------
    df.to_csv(output_path, index=False)

    print(f"Feature table saved successfully at: {output_path}")

    return df


# -----------------------------
# Execute script directly
# -----------------------------
if __name__ == "__main__":
    feature_engineering()
