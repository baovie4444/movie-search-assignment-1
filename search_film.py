import pandas as pd

def calculate_weighted_score(vandv):
    C = vandv['vote_average'].mean()
    m = 100

    def weighted_rating(vandv):
        v = vandv['vote_count']
        R = vandv['vote_average']
        return (v / (v + m) * R) + (m / (m + v) * C)

    vandv['weighted_score'] = vandv.apply(weighted_rating, axis=1)
    return vandv

def search_movies(vandv, search_criteria):
    filtered_df = vandv.copy()
    for field, term in search_criteria.items():
        filtered_df = filtered_df[filtered_df[field].astype(str).str.contains(term, case=False)]

    sorted_df = filtered_df.sort_values(by='weighted_score', ascending=False)
    return sorted_df

def export_to_csv(results):
    file_path = "D:/name.csv"
    results.head(10).to_csv(file_path, index=False)
    print(f"Results exported to {file_path}")

def main():
    vandv = pd.read_csv(r"C:\Users\Victus\Downloads\data.csv") 
    vandv_with_weighted_score = calculate_weighted_score(vandv)
    
    valid_fields = ['genres', 'original_title', 'overview', 'production_companies', 'production_countries', 'spoken_languages', 'title']
    
    search_criteria = {}
    num_fields = input("Enter number of fields to search by: ")
    
    while not num_fields.isdigit() or int(num_fields) > len(valid_fields) or int(num_fields)<=0:
        print("Invalid input. Please enter a valid number.")
        num_fields = input("Enter number of fields to search by: ")

    num_fields = int(num_fields)

    for i in range(num_fields):
        print("\nChoose a field by entering the corresponding number:")
        for idx, field in enumerate(valid_fields, 1):
            print(f"{idx}. {field}")
        
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

    results = search_movies(vandv_with_weighted_score, search_criteria)
    print("\nTop 10 results:")
    print(results[['genres', 'original_title', 'overview', 'production_companies', 'production_countries', 'spoken_languages', 'title','vote_average', 'vote_count', 'weighted_score']].head(10))
    
    export_to_csv(results)

main()
