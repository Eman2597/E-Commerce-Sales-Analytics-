# ===================================
#  Script Cleaning for Data Pipeline
# ====================================

import pandas as pd
import numpy as np
import os


# -----------------------------
# Helper to create safe file paths
# -----------------------------
def get_path(relative_path):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, relative_path)


# -----------------------------
# 1️: Clean Customers Table
# -----------------------------
def clean_customers(
    file_path=get_path("../data/raw/customers.csv"),
    output_path=get_path("../data/processed/customers_clean.csv"),
):
    customers = pd.read_csv(file_path)

    # Remove duplicate CustomerID
    customers = customers.drop_duplicates(subset=["CustomerID"], keep="first")

    # Convert Signup_Date to datetime
    customers["Signup_Date"] = pd.to_datetime(customers["Signup_Date"], errors="coerce")

    # Standardize Region column
    customers["Region"] = customers["Region"].str.strip().str.lower().str.title()

    # Save cleaned table
    customers.to_csv(output_path, index=False)

    return customers


# -----------------------------
# 2️: Clean Products Table
# -----------------------------
def clean_products(
    file_path=get_path("../data/raw/products.csv"),
    output_path=get_path("../data/processed/products_clean.csv"),
):
    products = pd.read_csv(file_path)

    # Remove duplicates
    products = products.drop_duplicates(subset=["ProductID"], keep="first")

    # Convert Price to numeric
    products["Price"] = pd.to_numeric(products["Price"], errors="coerce")

    # Standardize Category
    products["Category"] = products["Category"].str.strip().str.lower().str.title()

    # Save cleaned table
    products.to_csv(output_path, index=False)

    return products


# -----------------------------
# 3️: Clean Sales/Transactions Table
# -----------------------------
def clean_sales(
    file_path=get_path("../data/raw/sales_transactions.csv"),
    output_path=get_path("../data/processed/sales_transactions_clean.csv"),
):
    sales = pd.read_csv(file_path)

    # Remove duplicate TransactionID
    sales = sales.drop_duplicates(subset=["TransactionID"], keep="first")

    # Convert columns to appropriate types
    sales["Date"] = pd.to_datetime(sales["Date"], errors="coerce")
    sales["Quantity"] = pd.to_numeric(sales["Quantity"], errors="coerce")
    sales["Discount"] = pd.to_numeric(sales["Discount"], errors="coerce")

    # Clean Total_Amount and keep negative values
    sales["Total_Amount"] = (
        sales["Total_Amount"].astype(str).str.replace(r"[^0-9.-]", "", regex=True)
    )
    sales["Total_Amount"] = pd.to_numeric(sales["Total_Amount"], errors="coerce")

    # Clean text columns
    sales["ProductID"] = sales["ProductID"].astype(str).str.strip()
    sales["CustomerID"] = sales["CustomerID"].astype(str).str.strip()

    # Forward fill missing dates
    sales["Date"] = sales["Date"].ffill()

    # Save cleaned table
    sales.to_csv(output_path, index=False)

    return sales


# -----------------------------
# Execute cleaning when script runs directly
# -----------------------------
if __name__ == "__main__":
    clean_customers()
    clean_products()
    clean_sales()
    print("Data cleaning completed and saved to processed directory.")
