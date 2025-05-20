# NER_Project

**NER_Project** is a Python project that performs Named Entity Recognition (NER) using the code in the `main.py` file.

## Features

- Performs Named Entity Recognition on input text.
- Simple, contained implementation within a single script.
- Outputs results as `output.csv` inside the `output/` folder.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Devendra2803/NER_Project.git
   cd NER_Project/NER_Project
   ```

2. **Create and activate a virtual environment (optional but recommended)**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies** (if any; check imports in `main.py`):

   ```bash
   pip install -r requirements.txt
   ```

   *(If `requirements.txt` is not present, install the packages used in `main.py` manually.)*

## Usage

Run the NER program using:

```bash
python main.py
```

The extracted named entities and results will be saved as `output.csv` inside the `output/` folder.

Modify `main.py` to input your own text or integrate it into your pipeline.

## Project Structure

```
NER_Project/
└── NER_Project/
    ├── main.py          # Main script containing NER implementation
    └── output/
        └── output.csv   # CSV file containing NER results
```

## Contributing

Contributions and improvements are welcome. Please fork the repo and create pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
