import pandas as pd

def load_sales(path):
    with open(path, newline='', encoding='utf-8') as f:
        df = pd.read_csv(f)  # keys come from first row
        df.columns = df.columns.str.strip()
        df['price'] = df['price'].astype(float)
        df['quantity'] = df['quantity'].astype(int)
    return df
