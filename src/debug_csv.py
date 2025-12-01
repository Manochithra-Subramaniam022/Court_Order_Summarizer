# src/debug_csv.py

import pandas as pd

df = pd.read_csv("data/cleaned_data.csv")
print("📊 Total rows in CSV:", len(df))
print("🧠 Category counts:\n", df["Category"].value_counts())
