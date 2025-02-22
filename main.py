from pathlib import Path
from src.features.etl.extract import extract_data
from src.features.etl.transform import transform_data
from src.features.etl.load import load_data

def main():
    input_file = 'data/data.csv'     # Ensure this file is in the project root
    output_file = 'output.json' # Output file that will be created/overwritten

    # Step 1: Extract
    data = extract_data(input_file)
    if not data:
        print("No data extracted. Exiting.")
        return

    # Step 2: Transform
    transformed_data = transform_data(data)

    # Step 3: Load
    load_data(transformed_data, output_file)

if __name__ == '__main__':
    main()
