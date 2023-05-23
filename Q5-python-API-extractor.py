import requests
import pandas as pd
import json
api_link = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"

try:
    response = requests.get(api_link)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the JSON data from the response
        data = response.json()
        with open('data.json', 'w') as file:
            json.dump(data, file)

        key=list(data.keys())
        print(len(key))
        print(data[str(key[20])])
    else:
        print("Error: Failed to fetch data from the API.")
except Exception as e:
    print("failed to fetch the API , error : ",e)