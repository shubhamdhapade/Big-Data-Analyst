import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")
import os

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / 'data' / 'raw_sales.csv'
REPORT_OUTPUT = BASE_DIR / 'data' / 'sales_summary.csv'
PLOT_OUTPUT = BASE_DIR / 'sales_overview.png'

def load_and_clean_data() -> pd.DataFrame:
    if not DATA_FILE.exists():
        print(f"Error: File {DATA_FILE} not found.")
        return pd.DataFrame()

    df = pd.read_csv(DATA_FILE)
    df['Quantity'] = df['Quantity'].fillna(df['Quantity'].median())

    df['TotalRevenue'] = df['Quantity'] * df['UnitPrice']
    df['Date'] = pd.to_datetime(df['Date'])

    print("--- Cleaned Dataset Sample ---")
    print(df.head())
    
    return df

def generate_insights(df: pd.DataFrame) -> None:
    if df.empty:
        return

    print("\n--- Key Business Insights ---")
    
    category_revenue = df.groupby('ProductCategory')['TotalRevenue'].sum().reset_index()
    print("\nTotal Revenue by Product Category:")
    print(category_revenue)

    category_revenue.to_csv(REPORT_OUTPUT, index=False)
    print(f"\nSummary exported to '{REPORT_OUTPUT}'")
    
    region_revenue = df.groupby('Region')['TotalRevenue'].sum().reset_index()
    print("\nTotal Revenue by Region:")
    print(region_revenue)

    region_revenue.to_csv(BASE_DIR / 'data' / 'region_revenue_summary.csv', index=False)
    print(f"\nRegion revenue summary exported to '{BASE_DIR / 'data' / 'region_revenue_summary.csv'}'")

    payment_distribution = df['PaymentMethod'].value_counts()
    print("\nPayment Method Distribution:")
    print(payment_distribution)

    payment_distribution.to_csv(BASE_DIR / 'data' / 'payment_method_distribution.csv', index=True, header=['Count'])
    print(f"\nPayment method distribution exported to '{BASE_DIR / 'data' / 'payment_method_distribution.csv'}'")

    sales_trends = df.groupby(df['Date'].dt.to_period('M'))['TotalRevenue'].sum().reset_index()
    sales_trends['Date'] = sales_trends['Date'].dt.to_timestamp()
    print("\nMonthly Sales Trends:")
    print(sales_trends)

    sales_trends.to_csv(BASE_DIR / 'data' / 'monthly_sales_trends.csv', index=False)
    print(f"\nMonthly sales trends exported to '{BASE_DIR / 'data' / 'monthly_sales_trends.csv'}'")

    
def plot_visualizations(df: pd.DataFrame) -> None:
    if df.empty:
        return

    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    sns.barplot(data=df, x='ProductCategory', y='TotalRevenue', ax=axes[0], estimator=sum, errorbar=None, palette="viridis")
    axes[0].set_title('Total Revenue by Product Category')
    axes[0].set_xlabel('Category')
    axes[0].set_ylabel('Revenue ($)')

    payment_counts = df['PaymentMethod'].value_counts()
    axes[1].pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%', colors=sns.color_palette("pastel"))
    axes[1].set_title('Payment Method Breakdown')

    sales_trends = df.groupby(df['Date'].dt.to_period('M'))['TotalRevenue'].sum().reset_index()
    sales_trends['Date'] = sales_trends['Date'].dt.to_timestamp()
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=sales_trends, x='Date', y='TotalRevenue', marker='o', color='blue')
    plt.title('Monthly Sales Trends')
    plt.xlabel('Month')
    plt.ylabel('Revenue ($)')

    payment_distribution = df['PaymentMethod'].value_counts()
    plt.figure(figsize=(8, 5))
    sns.barplot(x=payment_distribution.index, y=payment_distribution.values, palette="muted")
    plt.title('Payment Method Distribution')
    plt.xlabel('Payment Method')
    plt.ylabel('Count')

    region_revenue = df.groupby('Region')['TotalRevenue'].sum().reset_index()
    plt.figure(figsize=(8, 5))
    sns.barplot(data=region_revenue, x='Region', y='TotalRevenue', palette="coolwarm")
    plt.title('Total Revenue by Region')
    plt.xlabel('Region')
    plt.ylabel('Revenue ($)')

    plt.tight_layout()
    plt.savefig(PLOT_OUTPUT)
    print(f"Visualization saved to '{PLOT_OUTPUT}'")
    plt.show()

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{'='*80}")
    print(f"{' Sales Data Analysis Dashboard ':^80}")
    print(f"{'='*80}")
    df = load_and_clean_data()
    generate_insights(df)
    plot_visualizations(df)