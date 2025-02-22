# Tech Assignment Python Project

A simple ETL (Extract, Transform, Load) pipeline to process CSV data into JSON.

## Table of Contents

1. Features
2. Project Structure
3. Installation
4. Usage
5. Testing
6. Troubleshooting

## Features

- **Dynamic CSV Parsing:**  
  Uses a helper function (`smart_cast`) to dynamically convert CSV string values to appropriate types.
- **Modular Design:**  
  Code is separated into distinct modules for extraction, transformation, and loading.
- **Feature-Based Structure:**  
  The ETL logic is organized under `src/features/etl` for clarity and maintainability.
- **Error Handling:**  
  Handles missing files and data conversion errors gracefully.
- **Testing:**  
  Unit tests using `pytest` are provided to validate each component of the ETL pipeline.

## Project Structure

```plaintext
tech-assignment-python/
├── data/
│   └── data.csv            # Input CSV file
├── output.json             # Output JSON file
├── main.py                 # Main entry point
├── README.md
├── requirements.txt
├── src/
│   └── features/
│       └── etl/
│           ├── __init__.py
│           ├── extract.py    # CSV extraction
│           ├── transform.py  # Data transformation
│           └── load.py       # JSON writing
└── tests/
    ├── __init__.py
    └── test_etl.py         # ETL unit tests
```
## Installation

1. Install Python 3.6+ from https://www.python.org/downloads/
3. Set up virtual environment:
   python3 -m venv venv
   source venv/bin/activate # Windows: venv\Scripts\activate
4. Install dependencies:
   pip install -r requirements.txt

## Usage

1. Add CSV file to data/input/data.csv
   Example CSV content:
   id,name,age,salary
   1,John,28,50000
   2,Alice,30,60000

2. Run the pipeline:
   python3 src/main.py

3. Check results in data/output/output.json

## Testing

Run tests with:
pytest tests/

## Troubleshooting


Contact
For questions or feedback, please contact Anesti Andoni at anestiandoniii@gmail.com.