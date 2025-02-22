def transform_data(data: list):
    """
    Transforms the data by adding a 'tax' field calculated as 20% of the salary.
    """
    transformed = []
    for row in data:
        if 'salary' in row and isinstance(row['salary'], (int, float)):
            row['tax'] = round(row['salary'] * 0.2, 2)
        transformed.append(row)
    return transformed
