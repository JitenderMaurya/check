import requests

# Define the URL and the parameters
url = "https://ypitchfit2.pythonanywhere.com/insights"
params = {"meta_data": "uk, airline, 2019, europe", "query": "revenue of diageo plc airlines for 2019"}

# Send a GET request with parameters
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Request failed with status code: {response.status_code}")