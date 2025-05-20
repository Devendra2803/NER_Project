from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import spacy
import csv
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
    logger.info("spaCy model loaded successfully.")
except Exception as e:
    logger.error(f"Error loading spaCy model: {e}")
    raise

# Create FastAPI app
app = FastAPI(title="Named Entity Recognition API")

# Output path
OUTPUT_CSV = r"C:\Users\USER\Documents\Projects\NER_Project\NER_Project\output\ner_output.csv"

@app.post("/extract")
async def extract_entities(file: UploadFile = File(...)):
    try:
        # Read and decode file
        content = await file.read()
        text = content.decode("utf-8")
        logger.info(f"Received text: {text}")

        # Process text
        doc = nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        if not entities:
            return JSONResponse(content={"message": "No entities found."}, status_code=200)

        # Ensure output folder exists
        os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)

        # Write to CSV
        with open(OUTPUT_CSV, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Entity Text", "Label"])
            for ent_text, label in entities:
                writer.writerow([ent_text, label])

        logger.info(f"Saved entities to CSV at {OUTPUT_CSV}")

        return {
            "message": "Entities extracted and saved to CSV.",
            "entities": [{"text": ent[0], "label": ent[1]} for ent in entities],
            "csv_path": OUTPUT_CSV
        }

    except Exception as e:
        logger.error(f"Error processing file: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
