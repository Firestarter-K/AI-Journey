import csv
from dataclasses import dataclass
from typing import Dict
from collections import defaultdict
from pathlib import Path

@dataclass
class Sale:
    product: str
    category: str
    price: float
    quantity: int

@dataclass
class TopProduct:
    price: float = 0.0
    product: str = ""

@dataclass
class Report:
    top_product: TopProduct
    top_product_mimic: Dict[str, float] = None
    category_total: Dict[str, float]
    sale_total: float = 0.0
    quantity_total: int = 0

def load_saledata(path):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)  # keys come from first row
        # row is a dict
        sales = [Sale(product=r['product'], category=r['category'], price=float(r['price']), quantity=int(r['quantity'])) for r in reader]
    return sales

def process_sales(sales):
    report = Report(top_product=TopProduct(), top_product_mimic=defaultdict(float), category_total=defaultdict(float), sale_total=0, quantity_total=0)
    for sale in sales:
        revenue = sale.price * sale.quantity
        report.category_total[sale.category] += revenue
        if report.top_product.price <= revenue:
            report.top_product.price = revenue
            report.top_product.product = sale.product
            report.top_product_mimic[sale.product] = revenue
        report.sale_total += revenue
        report.quantity_total += sale.quantity
    return report

def dispaly_report(report):
    print("===== SALES REPORT =====")
    print("\n" * 2)
    print(f"Total Revenue: ${report.sale_total:.2f}")
    print(f"Total Items Sold: {report.quantity_total}")
    print("\n")
    print("Revenue by Category:")
    for category, total in report.category_total.items():
        print(f"{category}: ${total:.2f}")
    print("\n")
    print("Top Product:")
    print(f"{report.top_product.product} - ${report.top_product.price:.2f}")
    print("\n")
    print("Top Product Comparison:")
    for product, revenue in report.top_product_mimic.items():
        print(f"{product} - ${revenue:.2f}")

csv_path = Path(__file__).parent / "sales.csv"
sales = load_saledata(csv_path)
report = process_sales(sales)
dispaly_report(report)





