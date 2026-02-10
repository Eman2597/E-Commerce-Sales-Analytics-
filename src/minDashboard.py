import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 1. تحميل البيانات
df = pd.read_csv(
    "../data/processed/fact_sales_features.csv", parse_dates=["Date", "Signup_Date"]
)

# 2. تجهيز البيانات (هذا الجزء كان ينقصك وهو سبب الـ NameError)
# استخراج السنة والشهر إذا لم تكن موجودة
df["Year"] = df["Date"].dt.year
df["Month_Name"] = df["Date"].dt.month_name()

region_md = df.groupby("Region")["Calculated_Revenue"].sum().reset_index()
category_md = df[["Category", "Calculated_Revenue"]]
monthly_md = (
    df.groupby(["Year", "Month_Name"])["Calculated_Revenue"].sum().reset_index()
)
corr_md = df.select_dtypes(include=["number"]).corr()


# 3. تعريف الدالة (نسخة واحدة محسنة)
def plot_interactive_dashboard(
    df, region_matrix, category_matrix, monthly_revenue, corr_matrix
):
    # -------- KPIs --------
    total_rev = df["Calculated_Revenue"].sum()
    total_orders = len(df)
    total_cust = df["CustomerID"].nunique()
    aov = total_rev / total_orders

    top_cat = region_matrix.sort_values(by="Calculated_Revenue", ascending=False).iloc[
        0
    ]["Region"]

    kpis_text = f"Total Revenue: ${total_rev:,.0f} | Orders: {total_orders} | Customers: {total_cust} | AOV: ${aov:,.0f}"

    # -------- Layout Setup --------
    fig = make_subplots(
        rows=3,
        cols=2,
        specs=[[{"colspan": 2}, None], [{}, {}], [{}, {}]],
        subplot_titles=(
            "KPIs Summary",
            "Revenue by Region",
            "Revenue by Category",
            "Correlation Matrix",
            "Monthly Trend",
        ),
    )

    # KPI Text
    fig.add_trace(
        go.Scatter(x=[0], y=[0], mode="text", text=[kpis_text], textfont=dict(size=16)),
        row=1,
        col=1,
    )

    # Bar Chart
    for trace in px.bar(
        region_matrix, x="Region", y="Calculated_Revenue", color="Region"
    ).data:
        fig.add_trace(trace, row=2, col=1)

    # Boxplot
    for trace in px.box(
        category_matrix, x="Category", y="Calculated_Revenue", color="Category"
    ).data:
        fig.add_trace(trace, row=2, col=2)

    # Heatmap
    fig.add_trace(
        go.Heatmap(
            z=corr_matrix.values,
            x=corr_matrix.columns,
            y=corr_matrix.columns,
            colorscale="RdBu",
        ),
        row=3,
        col=1,
    )

    # Line Chart
    for trace in px.line(
        monthly_revenue,
        x="Month_Name",
        y="Calculated_Revenue",
        color="Year",
        markers=True,
    ).data:
        fig.add_trace(trace, row=3, col=2)

    fig.update_layout(height=900, title_text="E-Commerce Dashboard", showlegend=False)
    fig.show()


# 4. استدعاء الدالة
plot_interactive_dashboard(df, region_md, category_md, monthly_md, corr_md)
