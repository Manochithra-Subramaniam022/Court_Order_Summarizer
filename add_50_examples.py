# add_50_examples.py
import pandas as pd
from datetime import datetime, timedelta
import random
import os

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

# Load existing data
df = pd.read_csv("data/cleaned_data.csv")

# Generate synthetic examples
new_data = []
base_date = datetime(2024, 1, 1)

judgment_texts = [
    "The Supreme Court upheld the right to free speech in digital platforms.",
    "The High Court ruled that land acquisition must follow due process.",
    "The ruling clarified provisions of the environmental protection act.",
    "The judgment emphasized gender equality in workplace policies.",
    "The court recognized climate change as a constitutional concern."
]

policy_texts = [
    "The government announced a new education policy for rural schools.",
    "The cyber security framework was revised to prevent data breaches.",
    "The renewable energy policy aims to reduce carbon emissions by 2030.",
    "The health policy ensures affordable treatment for chronic diseases.",
    "The housing policy prioritizes urban poor in metropolitan cities."
]

for i in range(25):
    date = (base_date + timedelta(days=i)).strftime("%Y-%m-%d")
    title = f"Judgment Update {i+1}"
    text = random.choice(judgment_texts)
    new_data.append([date, title, "Judgment", text, text.lower().replace(" ", "")])

for i in range(25):
    date = (base_date + timedelta(days=30+i)).strftime("%Y-%m-%d")
    title = f"Policy Update {i+1}"
    text = random.choice(policy_texts)
    new_data.append([date, title, "Policy", text, text.lower().replace(" ", "")])

# Append to original dataframe
df_new = pd.DataFrame(new_data, columns=df.columns)
df = pd.concat([df, df_new], ignore_index=True)

# Save updated dataset
df.to_csv("data/cleaned_data.csv", index=False)

print("✅ 50 new synthetic examples added successfully!")
print(f"📊 New dataset size: {len(df)}")
