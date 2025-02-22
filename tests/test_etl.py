import json
from pathlib import Path
from src.features.etl.extract import extract_data
from src.features.etl.transform import transform_data
from src.features.etl.load import load_data

def test_extract_data(tmp_path):
    # Create a temporary CSV file
    csv_content = """id,name,age,salary
1,John,28,50000
2,Alice,30,60000
"""
    file_path = tmp_path / "test_data.csv"
    file_path.write_text(csv_content)

    data = extract_data(str(file_path))
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]['id'] == 1
    assert data[0]['name'] == "John"

def test_transform_data():
    data = [
        {"id": 1, "name": "John", "age": 28, "salary": 50000},
        {"id": 2, "name": "Alice", "age": 30, "salary": 60000},
    ]
    transformed = transform_data(data)
    assert "tax" in transformed[0]
    assert transformed[0]["tax"] == 10000.0

def test_load_data(tmp_path):
    # Prepare sample data
    data = [{"id": 1, "name": "John", "age": 28, "salary": 50000, "tax": 10000}]
    output_file = tmp_path / "output.json"
    load_data(data, str(output_file))
    
    # Verify the file exists and contains the correct JSON
    assert output_file.exists()
    with open(output_file, "r", encoding="utf-8") as file:
        loaded_data = json.load(file)
    assert loaded_data == data

def test_extract_data_file_not_found(capsys):
    # Provide a non-existent file path to test error handling.
    data = extract_data("non_existent_file.csv")
    captured = capsys.readouterr().out
    # Check that the error message was printed and data is empty.
    assert "Error: File 'non_existent_file.csv' not found." in captured
    assert data == []

def test_transform_data_missing_salary():
    # Provide a record without a salary field.
    data = [{"id": 1, "name": "John", "age": 28}]
    transformed = transform_data(data)
    # Expect that tax is set to None because salary is missing.
    assert transformed[0].get("tax") is None

def test_transform_data_invalid_salary():
    # Provide a record with a non-numeric salary.
    data = [{"id": 1, "name": "John", "age": 28, "salary": "not_a_number"}]
    transformed = transform_data(data)
    # Expect that tax is set to None because the salary cannot be processed.
    assert transformed[0].get("tax") is None

def test_load_data_error(tmp_path, monkeypatch):
    # Create sample data
    sample_data = [{"id": 1, "name": "John", "age": 28, "salary": 50000, "tax": 10000}]
    # Create a temporary directory and then remove write permissions to simulate a write error.
    temp_dir = tmp_path / "no_write"
    temp_dir.mkdir()
    output_file = temp_dir / "output.json"
    # Monkey-patch open to raise an exception when attempting to write.
    def fake_open(*args, **kwargs):
        raise IOError("Simulated write error")
    monkeypatch.setattr("builtins.open", fake_open)
    # Call load_data and capture the output.
    load_data(sample_data, str(output_file))
    # The test checks that our error handling message (or behavior) is triggered.
    # In this example, we simply ensure that the function doesn't crash.