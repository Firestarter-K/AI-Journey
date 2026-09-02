
from operator import inv


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

inventory = dict()
inventory.setdefault("Clothing", []).append({"name": "Shirt", "amount": 20.0})
inventory.setdefault("Clothing", []).append({"name": "Pants", "amount": 35.5})
inventory.setdefault("Food", []).append({"name": "Icecream", "amount": 4.5})
inventory.setdefault("Food", []).append({"name": "Pizza", "amount": 12.5})
inventory.setdefault("Electronics", []).append({"name": "Microwave", "amount": 129.9})
inventory.setdefault("Furniture", []).append({"name": "Storage", "amount": 93.9})

while True:
    category = input("Enter category: ").strip()
    if category:
        break
    print("Please enter a value.")

key = category.strip().title()
total = expenses_by_category(key, inventory)
print(f"Total amount for {key}: {total}")
