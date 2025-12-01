import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.preprocessing import clean_text
import pandas as pd

# Load the original dataset
df = pd.read_csv("data/sample_legal_policy_data.csv")

# Apply text cleaning
df['Cleaned_Text'] = df['Document_Text'].apply(clean_text)

# Save the cleaned dataset
df.to_csv("data/cleaned_data.csv", index=False)

print("✅ Data cleaned and saved to data/cleaned_data.csv")
