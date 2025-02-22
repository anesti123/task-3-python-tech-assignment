import csv

def smart_cast(value):
    """
    Attempts to cast a CSV string value to an int or float.
    If the value is None (or an empty string, if desired) or if both conversions fail,
    returns the value as-is.
    """
    if value is None or value == "":
        return value
    for cast in (int, float):
        try:
            return cast(value)
        except (ValueError, TypeError):
            continue
    return value


def extract_data(file_path: str):
    """
    Reads a CSV file and returns a list of dictionaries.
    Dynamically processes each field without hard-coded column names.
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = []
            for row in reader:
                # Dynamically cast each value using smart_cast
                processed_row = {key: smart_cast(value) for key, value in row.items()}
                data.append(processed_row)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
