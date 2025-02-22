import json

def load_data(data: list, output_file: str):
    """
    Writes the transformed data to a JSON file with indentation for readability.
    """
    try:
        with open(output_file, mode='w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        print(f"Data successfully loaded into {output_file}")
    except Exception as e:
        print(f"Error writing to {output_file}: {e}")
