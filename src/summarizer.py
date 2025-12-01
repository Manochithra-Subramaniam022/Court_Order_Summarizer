# src/summarizer.py
import spacy
from transformers import pipeline

# Load spaCy model for NER
nlp = spacy.load("en_core_web_sm")

# Hugging Face summarizer
summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")

def summarize_order(text):
    try:
        # Generate summary
        summary = summarizer(text, max_length=60, min_length=20, do_sample=False)[0]['summary_text']
    except Exception as e:
        return f"❌ Summarization failed: {str(e)}"

    # Extract entities
    doc = nlp(text)
    parties = []
    sections = []
    dates = []
    acts = []

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            parties.append(ent.text)
        elif ent.label_ in ["DATE"]:
            dates.append(ent.text)
        elif "Act" in ent.text or "IPC" in ent.text:
            acts.append(ent.text)
        elif "Section" in ent.text:
            sections.append(ent.text)

    key_info = {
        "Summary": summary,
        "Petitioner": parties[0] if parties else "Not Found",
        "Date": dates[0] if dates else "Not Found",
        "Section": sections[0] if sections else "Not Mentioned",
        "Act": acts[0] if acts else "Not Mentioned"
    }

    return key_info
