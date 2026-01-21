Interactive Sales Dashboard

Week 6 – Data Visualization Project

Project Overview

This project focuses on building an Interactive Sales Dashboard to analyze and present sales data in a clear and meaningful way. Instead of looking at raw numbers in a table, the goal is to use visualizations to understand how sales vary across regions, products, and time.

The dashboard combines statistical charts created using Seaborn with interactive charts built using Plotly. This helps in identifying trends, patterns, and outliers in the data and makes the analysis easier to interpret, even for non-technical users.

Project Goals

Visualize sales performance across different regions and products

Understand the distribution and variability of sales values

Identify relationships between quantity, price, and total sales

Create interactive charts for better data exploration

Present insights using a clean and professional dashboard layout

Dataset Information

The project uses a sales dataset stored in sales_data.csv.

Columns included in the dataset:

Date – Date of the sale

Product – Name of the product sold

Quantity – Number of units sold

Price – Price per unit

Customer_ID – Unique identifier for each customer

Region – Sales region

Total_Sales – Total sales amount for each transaction

Tools and Technologies

Python for data analysis and visualization

Pandas for data cleaning and manipulation

Seaborn for statistical visualizations

Matplotlib for plotting support

Plotly for interactive charts and dashboard creation

Project Folder Structure
sales-dashboard/
│
├── dashboard.ipynb          # Jupyter notebook with full analysis
├── dashboard.py             # Python script to generate visualizations
├── requirements.txt         # List of required libraries
├── dashboard_demo.gif       # Demo of the dashboard workflow
│
├── visualizations/
│   ├── sales_distribution.png
│   ├── boxplot_category_sales.png
│   ├── violinplot_region_sales.png
│   └── correlation_heatmap.png
│
└── README.md

How to Run the Project
Step 1: Install Dependencies
pip install -r requirements.txt

Step 2: Run the Notebook
jupyter notebook dashboard.ipynb

Step 3: Run the Python Script
python dashboard.py


Running the script will generate all the required visualizations and store them in the visualizations folder.

Explanation of Visualizations
Sales Distribution

This plot shows how sales values are distributed overall. It helps in understanding whether most sales are concentrated in a particular range or spread widely.

Box Plot (Product-wise Sales)

The box plot highlights the median sales value for each product and clearly shows outliers. This makes it easy to compare product performance.

Violin Plot (Region-wise Sales)

The violin plot provides a detailed view of how sales are distributed across different regions. It combines both distribution shape and summary statistics.

Correlation Heatmap

The heatmap shows relationships between numerical variables such as quantity, price, and total sales. This helps in identifying which factors influence sales the most.

Interactive Dashboard

The interactive dashboard allows users to explore sales trends over time and compare performance across products and regions using hover and interactive features.# sales-dashboard
