import requests
#requests is used to acces the given link and download data
import pandas as pd
#pandas is used for dataframe related operations

def JSON_DWONLOADER(url, file_path):
    #accessing the link and check weather if its sucesfull
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Data downloaded successfully and saved at {file_path}")
    else:
        print("Failed to download the data.")

def CONERT_TO_CSV(json_file_path, csv_file_path):
    #reads the downloaded json file
    df = pd.read_json(json_file_path)
    #converts it into csv file
    df.to_csv(csv_file_path, index=False)
    print(f"Data converted and saved as CSV at {csv_file_path}")

url = "https://data.nasa.gov/resource/y77d-th95.json"

# File paths for downloaded JSON and CSV files
json_path = "data.json"
csv_path = "data.csv"


#calls the function to download data
JSON_DWONLOADER(url, json_path)
# calls the function to convert the data to CSV
CONERT_TO_CSV(json_path, csv_path)
