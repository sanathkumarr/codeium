# app/utils/ner_parser.py
import spacy

nlp = spacy.load("en_core_web_lg")

def extract_entities(text):
    doc = nlp(text)
    entities = {
        "name": None,
        "email": None,
        "phone": None,
        "skills": []
    }
    for ent in doc.ents:
        if ent.label_ == "PERSON" and not entities["name"]:
            entities["name"] = ent.text
        elif ent.label_ == "EMAIL" and not entities["email"]:
            entities["email"] = ent.text
        elif ent.label_ == "PHONE" and not entities["phone"]:
            entities["phone"] = ent.text
        elif ent.label_ == "SKILL":
            entities["skills"].append(ent.text)
    return entities
