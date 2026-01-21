# dashboard.py
# Interactive Sales Dashboard
# Week 6: Data Visualization Mastery

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


def load_data(path="sales_data.csv"):
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'])
    return df


def seaborn_visualizations(df):
    sns.set_style("whitegrid")

    # Sales Distribution
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Sales'], kde=True)
    plt.title("Sales Distribution")
    plt.savefig("visualizations/sales_distribution.png")
    plt.close()

    # Box Plot
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='Category', y='Sales', data=df)
    plt.title("Sales Distribution by Category")
    plt.savefig("visualizations/boxplot_category_sales.png")
    plt.close()

    # Violin Plot
    plt.figure(figsize=(8, 5))
    sns.violinplot(x='Region', y='Sales', data=df)
    plt.title("Sales Distribution by Region")
    plt.savefig("visualizations/violinplot_region_sales.png")
    plt.close()

    # Heatmap
    corr = df.select_dtypes(include='number').corr()
    plt.figure(figsize=(6, 4))
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.savefig("visualizations/correlation_heatmap.png")
    plt.close()


def interactive_dashboard(df):
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=[
            "Sales Trend",
            "Sales by Category",
            "Sales Distribution",
            "Region Performance"
        ]
    )

    fig.add_trace(
        go.Scatter(x=df['Date'], y=df['Sales'], mode='lines', name='Sales'),
        row=1, col=1
    )

    fig.add_trace(
        go.Bar(x=df['Category'], y=df['Sales'], name='Category Sales'),
        row=1, col=2
    )

    fig.add_trace(
        go.Histogram(x=df['Sales'], name='Sales Distribution'),
        row=2, col=1
    )

    fig.add_trace(
        go.Box(x=df['Region'], y=df['Sales'], name='Region Sales'),
        row=2, col=2
    )

    fig.update_layout(
        height=800,
        title_text="Interactive Sales Dashboard"
    )

    fig.show()


def main():
    import os
    os.makedirs("visualizations", exist_ok=True)

    df = load_data()
    seaborn_visualizations(df)
    interactive_dashboard(df)


if __name__ == "__main__":
    main()
