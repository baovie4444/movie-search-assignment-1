import pandas as pd
import ast

# Function to extract the names of the genres, production companies, production countries, and spoken languages
def extract_names(data_str):
    try:
        data_list = ast.literal_eval(data_str)
        names = [item['name'] for item in data_list]
        names = ', '.join(names)
        return names
    except (ValueError, TypeError):
        return ''

# Function to transform the data
def transform_data(input_file, output_file):
    # Load the input file
    data = pd.read_csv(input_file, low_memory=False)
    
    # Apply the transformations 
    data['genres'] = data['genres'].apply(extract_names)
    data['production_companies'] = data['production_companies'].apply(extract_names)
    data['production_countries'] = data['production_countries'].apply(extract_names)
    data['spoken_languages'] = data['spoken_languages'].apply(extract_names)

    # Select only the required columns
    cleaned_columns = ['genres', 'original_title', 'overview', 'production_companies', 'production_countries', 'spoken_languages', 'title', 'vote_average', 'vote_count']
    transformed_data = data[cleaned_columns]
    
    # Remove duplicate rows based on the original_title column
    transformed_data = transformed_data.drop_duplicates(subset=['original_title'])
    
    # Save the transformed data to the output file
    transformed_data.to_csv(output_file, index=False)
    print(f"Data has been transformed and saved to {output_file}")

# Can change to your on-device directory
input_file = r"C:\Users\Victus\Downloads\movies_metadata (1).csv"
output_file = r"C:\Users\Victus\Downloads\data.csv"
transform_data(input_file, output_file)
