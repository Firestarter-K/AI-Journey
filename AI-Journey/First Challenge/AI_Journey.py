
from collections import defaultdict

def total_expenses(inventory):
    total = 0
    for item in inventory:
        total += item['amount']
    return total

def expenses_by_category(category, inventory):
    return total_expenses(inventory.get(category, []))

items = [
    {"name": "Shirt", "amount": 20.0, "category": "Clothing"},
    {"name": "Pants", "amount": 35.5, "category": "Clothing"},
    {"name": "Icecream", "amount": 4.5, "category": "Food"},
    {"name": "Pizza", "amount": 12.5, "category": "Food"},
    {"name": "Microwave", "amount": 129.9, "category": "Electronics"},
    {"name": "Storage", "amount": 93.9, "category": "Furniture"},
]

inventory = defaultdict(list)
for it in items:
    inventory[it['category']].append(it)

while True:
    category = input("Enter category: ").strip()
    if category:
        break
    print("Please enter a value.")

key = category.strip().title()
total = expenses_by_category(key, inventory)

if total == 0:
    print(f"{key} was not found in inventory")
else:
    print(f"Total amount for {key}: {total}")
