🧠 Named Entity Recognition (Python + spaCy)

This project is a simple Named Entity Recognition (NER) system. It processes raw text to identify named entities such as people, organizations, and locations, and saves the output as a CSV file for analysis.

____________________________________________________________________________________________

🚀 Features

📄 Performs Named Entity Recognition on predefined input text.

🧠 Uses spaCy NLP model for entity detection.

📤 Saves extracted entities and their labels to a CSV file.

💡 Easy to run from a single script: `main.py`

____________________________________________________________________________________________

📁 Project Structure

```
Named_Entity_Recognition/
├── main.py                 # Main script for NER processing
├── output/
│   └── output.csv          # CSV file containing named entities
├── requirements.txt        # Required Python packages
└── README.md
```

____________________________________________________________________________________________

⚙️ Setup Instructions

1. ✅ Clone the repository

```bash
git clone https://github.com/Devendra2803/NER_Project.git
cd NER_Project
```

2. 📦 Install dependencies

```bash
pip install -r requirements.txt
```

> Note: Make sure `spaCy` is installed and the required model is downloaded.
```bash
python -m spacy download en_core_web_sm
```

_______________________________________________________________________________________________

▶️ Running the App

### Open the terminal and run:

```bash
python main.py
```

This will:

- Load the default English NLP model (`en_core_web_sm`)
- Run NER on the hardcoded sample text
- Save the entities and their labels in `output/output.csv`

____________________________________________________________________________________________

📝 Output File Format

The output CSV file (`output/output.csv`) is formatted as:

```
Entity,Label
"Apple","ORG"
"New York","GPE"
"John Smith","PERSON"
```

Each row contains a detected entity and its classification.

____________________________________________________________________________________________

🙌 Acknowledgements

- Python  
- spaCy NLP Library  
- pandas (for CSV writing)
