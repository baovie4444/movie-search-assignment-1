# README.md

## Movie Data Processing and Analysis

This repository contains two Python programs for processing and analyzing movie data. 

### Program 1: data_cleaning.py

#### Description
The first program is designed to clean movie data by extracting relevant information such as genres, production companies, production countries, and spoken languages and remove duplicate rows

#### Usage
```python
import pandas as pd
import ast

# Function to extract the names of the genres, production companies, production countries, and spoken languages
def extract_names(data_str):
    # ... (code details)

# Function to transform the data
def transform_data(input_file, output_file):
    # ... (code details)

input_file = r"C:\Users\Victus\Downloads\movies_metadata (1).csv"
output_file = r"C:\Users\Victus\Downloads\data.csv"
transform_data(input_file, output_file)
```

### Program 2: Movie Search and Weighted Scoring

#### Description
The second program performs movie search based on user-defined criteria and calculates a weighted score for each movie. The results can be exported to a CSV file.

#### Usage
```python
import pandas as pd

def calculate_weighted_score(vandv):
    # ... (code details)

def search_movies(vandv, search_criteria):
    # ... (code details)

def export_to_csv(results):
    # ... (code details)

def get_input(valid_fields, prompt, max_val):
    # ... (code details)

def main():
    # ... (code details)

main()
```

### Program Usage

1. **Data Transformation**:
   - Ensure you have `pandas` and `ast` installed in your Python environment.
   - Modify `input_file` and `output_file` variables with appropriate file paths.
   - Execute the program.

2. **Movie Search and Weighted Scoring**:
   - Ensure you have `pandas` installed in your Python environment.
   - Modify the file path in `pd.read_csv()` to point to your input CSV file.
   - Execute the program.
   - Follow on-screen instructions to perform a search based on movie fields.

### Sample Data

You can use the provided `movies_metadata.csv` as sample input data for testing the programs. Make sure to adjust file paths in the programs accordingly.

### Note

- The code snippets provided in the README are for illustrative purposes. Make sure to adapt the file paths and adjust any other parameters as per your specific use case.

### License

This code is provided to free public use. Feel free to modify and use it according to your needs.

---

Feel free to modify this README to add any specific details or instructions based on your requirements.
