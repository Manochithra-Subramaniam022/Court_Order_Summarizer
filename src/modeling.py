# src/modeling.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

# 1. Load dataset
df = pd.read_csv("data/cleaned_data.csv")

print(f"📊 Total training examples: {len(df)}")
print("🧠 Category distribution:\n", df["Category"].value_counts())

# 2. Features and labels
X = df["Cleaned_Text"]
y = df["Category"]

# 3. TF-IDF Vectorization
vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform(X)

# 4. Train-test split with stratification
X_train, X_test, y_train, y_test = train_test_split(
    X_tfidf, y, test_size=0.2, stratify=y, random_state=42
)

print("\n🔍 Train distribution:\n", y_train.value_counts())
print("🔍 Test distribution:\n", y_test.value_counts())

# 5. Train Naive Bayes model
model = MultinomialNB()
model.fit(X_train, y_train)

# 6. Predictions
y_pred = model.predict(X_test)

# src/modeling.py (add these lines after the classification report)

from summarizer import generate_summary

print("\n📝 Summaries of Test Examples:\n")
for i, text in enumerate(X_test[:3]):  # Show summaries for 3 test docs
    print(f"Document {i+1} ({y_test.iloc[i]}):")
    print("Original Text:", text[:300], "...")
    print("Summary:", generate_summary(text))
    print("-" * 80)


# 7. Evaluation
print("\n📊 Classification Report:")
print(classification_report(y_test, y_pred))

print("✅ Model training and evaluation complete.")
