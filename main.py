import sys
import os
import pandas as pd

# add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.preprocessing import clean_text

if __name__ == "__main__":
    # --- Test with examples ---
    examples = [
        "The Court delivered a significant judgment on 15th March 2023, regarding data privacy!",
        "On April 2nd, 2021, the policy draft was submitted by the central government for review.",
        "Judgment was made under Section 377A of the IPC and cited previous similar rulings.",
        "This case deals with land acquisition in rural areas—impacting 150+ families!",
        "Justice delayed is justice denied. Therefore, the appeal was fast-tracked.",
        "The Digital India Bill 2023 replaces old IT policies, with new regulations on surveillance.",
        "A law passed in 2022 bans all forms of crypto mining in protected zones."
    ]

    print("\n🔹 Cleaning Example Sentences:")
    for i, text in enumerate(examples, start=1):
        cleaned = clean_text(text)
        print(f"\nExample {i}:")
        print("Original:", text)
        print("Cleaned :", cleaned)

    # --- Clean the full dataset ---
    print("\n🔹 Cleaning Full Dataset...")
    df = pd.read_csv("data/sample_legal_policy_data.csv")
    df['Cleaned_Text'] = df['Document_Text'].apply(clean_text)
    df.to_csv("data/cleaned_data.csv", index=False)
    print("✅ Full dataset cleaned and saved to data/cleaned_data.csv")
