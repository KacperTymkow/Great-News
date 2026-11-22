import time
import requests

URL = "https://api.gdeltproject.org/api/v2/doc/doc"

query = {
    "query": "science sourcelang:English",
    "mode": "artlist",
    "format": "json",
    "maxrecords": 5,
    "timespan": "24h",
}

time.sleep(5)

try: 
    resp = requests.get(URL, params=query, timeout=30)
    resp.raise_for_status() 
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    print("Retrying in 5 seconds...")
    time.sleep(5)
    resp = requests.get(URL, params=query, timeout=30)
    resp.raise_for_status()  

print(resp.url)
print(resp.status_code)
print(resp.text[:500]) # Print the first 500 characters of the response text