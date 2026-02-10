# ===================================
#  Phase 2: Data Modeling (Merging)
# ===================================
import pandas as pd


def merge_tables(
    sales_path="../data/processed/sales_transactions_clean.csv",
    customers_path="../data/processed/customers_clean.csv",
    products_path="../data/processed/products_clean.csv",
    output_path="../data/processed/fact_sales_merged.csv",
):
    # Load cleaned tables
    sales = pd.read_csv(sales_path, parse_dates=["Date"])
    customers = pd.read_csv(customers_path, parse_dates=["Signup_Date"])
    products = pd.read_csv(products_path)

    # Merge with customers
    df = sales.merge(customers, on="CustomerID", how="left")

    # Merge with products
    df = df.merge(products, on="ProductID", how="left")

    # Save merged fact table
    df.to_csv(output_path, index=False)

    print("Merged table saved to:", output_path)
    print("Final shape:", df.shape)

    return df


# -----------------------------
# Execute when script runs
# -----------------------------
if __name__ == "__main__":
    merge_tables()
