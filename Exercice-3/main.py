import os
from utils.api_utils import fetch_api_data
from utils.csv_utils import modify_csv, export_to_csv, uppercase_row
from utils.json_utils import export_to_json

def print_section_title(title: str):
    """
    Affiche un titre de section bien formaté avec une ligne de séparation.
    """
    print(f"\n{'-' * 20} {title} {'-' * 20}\n")

def main():
    # ----- Question 1 -----
    print_section_title("Question 1 : Requête API")
    api_url = "https://jsonplaceholder.typicode.com/posts/1"
    api_data = fetch_api_data(api_url)
    print(api_data)

    # ----- Question 2 -----
    print_section_title("Question 2 : Modification CSV")
    input_csv = "./assets/input.csv"
    output_csv = "./assets/output_modified.csv"
    modify_csv(input_csv, output_csv, uppercase_row)

    # ----- Question 3 -----
    print_section_title("Question 3 : Export JSON")
    export_to_json(api_data, "./assets/output.json")

    # ----- Question 4 -----
    print_section_title("Question 4 : Export CSV")
    export_to_csv(api_data, "./assets/output.csv")

if __name__ == "__main__":
    main()
