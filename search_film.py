import pandas as pd

# Function to calculate the weighted score for each movie
def calculate_weighted_score(vandv):
    # Calculate the mean vote average for the dataset
    C = vandv['vote_average'].mean()
    # Set a minimum threshold for vote count
    m = 100

    # Calculate weighted rating for a movie
    def weighted_rating(vandv):
        v = vandv['vote_count']
        R = vandv['vote_average']
        return (v / (v + m) * R) + (m / (m + v) * C)

    # Apply weighted rating calculation to all movies
    vandv['weighted_score'] = vandv.apply(weighted_rating, axis=1)
    return vandv

# Function to search movies based on given criteria
def search_movies(vandv, search_criteria):
    # Copy the dataset to not modify the original
    filtered_df = vandv.copy()
    
    # Filter movies based on the provided search criteria
    for field, term in search_criteria.items():
        filtered_df = filtered_df[filtered_df[field].astype(str).str.contains(term, case=False)]

    # Sort the filtered movies by weighted score in descending order
    sorted_df = filtered_df.sort_values(by='weighted_score', ascending=False)
    return sorted_df

# Function to export top 10 results to a CSV file
def export_to_csv(results):
    # Can change to your on-device directory
    file_path = "D:/name.csv"
    results.head(10).to_csv(file_path, index=False)
    print(f"Results exported to {file_path}")

# Main function to execute the movie search functionality
def main():
    # Load the dataset from the given path
    # Can change to your on-device directory
    vandv = pd.read_csv(r"C:\Users\Victus\Downloads\data.csv")
    
    # Calculate the weighted score for all movies
    vandv_with_weighted_score = calculate_weighted_score(vandv)
    
    # List of valid fields the user can search by
    valid_fields = ['genres', 'original_title', 'overview', 'production_companies', 'production_countries', 'spoken_languages', 'title']
    
    search_criteria = {}
    
    # Ask the user for the number of fields they want to search by
    num_fields = input("Enter number of fields to search by: ")
    
    # Input validation for number of fields
    while not num_fields.isdigit() or int(num_fields) > len(valid_fields) or int(num_fields)<=0:
        print("Invalid input. Please enter a valid number.")
        num_fields = input("Enter number of fields to search by: ")

    num_fields = int(num_fields)

    # Iterate through each field, prompting the user for their search terms
    for i in range(num_fields):
        print("\nChoose a field by entering the corresponding number:")
        for idx, field in enumerate(valid_fields, 1):
            print(f"{idx}. {field}")
        
        # Input validation for field selection and search term input
        try:
            field_number = input(f"Enter number for field {i+1}: ")
            
            while not field_number.isdigit() or int(field_number) <=0 or int(field_number) > len(valid_fields):
                print("Invalid number entered. Please try again.")
                field_number = input(f"Enter number for field {i+1}: ")
            field_number = int(field_number)
            field = valid_fields[int(field_number) - 1]
            term = input(f"Enter search term for {field}: ")
            search_criteria[field] = term
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

    # Fetch search results based on provided criteria
    results = search_movies(vandv_with_weighted_score, search_criteria)
    
    # Display the top 10 results
    print("\nTop 10 results:")
    print(results[['genres', 'original_title', 'overview', 'production_companies', 'production_countries', 'spoken_languages', 'title','vote_average', 'vote_count', 'weighted_score']].head(10))
    
    # Export the top 10 results to a CSV file
    export_to_csv(results)

main()

