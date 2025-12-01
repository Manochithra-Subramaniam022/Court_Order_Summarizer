import pandas as pd
import gensim
from gensim import corpora
from nltk.tokenize import word_tokenize

# Step 1: Load cleaned data
df = pd.read_csv("data/cleaned_data.csv")

# Step 2: Tokenize the cleaned text column
texts = [word_tokenize(doc) for doc in df['Cleaned_Text'].dropna()]

# Step 3: Create dictionary and document-term matrix
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

# Step 4: Build LDA model
lda_model = gensim.models.LdaModel(
    corpus=corpus,
    id2word=dictionary,
    num_topics=3,
    passes=10,
    random_state=42
)

# Step 5: Display topics
print("\n🔍 Top Topics:")
topics = lda_model.print_topics(num_words=5)
for topic in topics:
    print(topic)
