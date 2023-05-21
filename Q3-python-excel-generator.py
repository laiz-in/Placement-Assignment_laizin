import requests
#request used to accesS the link 
import pandas as pd
#pandas for json file and writing excel

#creates a function that takes 3 parameters and 
def data_extractor(url, json_path, excel_path):
    try:
        response = requests.get(url)
        #if the link is succesfully loaded then it will return the status code 200
        if response.status_code == 200:
            with open(json_path, 'wb') as file:
                file.write(response.content)
                #json file saved at given path
            print(f"JSON file downloaded successfully and saved at {json_path}.\n\n")
        else:
            print("Failed to download the JSON file.")
        
        #reads the json file
        data_excel = pd.read_json(json_path)
        #tolist() is used to convert the values to list
        data = data_excel['pokemon'].tolist()

        #creates a dataframe of the list we created
        df = pd.DataFrame(data)

        #convertibg the dataframe into excel file with dictionary keys as column names
        df.to_excel(excel_path, index=False)
        
        df = pd.read_excel(excel_path, sheet_name='Sheet1')
        df.fillna("NA", inplace=True)
        df.to_excel(excel_path, sheet_name='Sheet1', index=False)
        #replacing empty cells with 'NA'

        #saves the excel sheet at the given path
        print(f"Excel file saved successfully at {excel_path}.")

    except Exception as e:
        print("Error occurred while accessing the link. Error: ", e)


url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
json_path = "data.json"
excel_path = "data.xlsx"
data_extractor(url, json_path, excel_path)
#calling the function with url , path fro json file and path for ne wecel file
