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
    topProduct: TopProduct
    categoryTotal: Dict[str, float]
    totalSale: float = 0.0
    totalQuantity: int = 0

csv_path = Path(__file__).parent / "sales.csv"
with open(csv_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)  # keys come from first row
    # row is a dict
    sales = [Sale(product=r['product'], category=r['category'], price=float(r['price']), quantity=int(r['quantity'])) for r in reader]

report = Report(topProduct=TopProduct(), categoryTotal=defaultdict(float),totalSale=0,totalQuantity=0)
for sale in sales:
    report.categoryTotal[sale.category] += sale.price * sale.quantity

    if report.topProduct.price <= sale.price * sale.quantity:
        report.topProduct.price = sale.price * sale.quantity
        report.topProduct.product = sale.product

    report.totalSale += sale.price * sale.quantity
    report.totalQuantity += sale.quantity

print("===== SALES REPORT =====")
print("\n" * 2)
print(f"Total Revenue: ${report.totalSale:.2f}")
print(f"Total Items Sold: {report.totalQuantity}")
print("\n")
print("Revenue by Category:")
for category, total in report.categoryTotal.items():
    print(f"{category}: ${total:.2f}")
print("\n")
print("Top Product:")
print(f"{report.topProduct.product} - ${report.topProduct.price:.2f}")





