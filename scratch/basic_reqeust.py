import requests


url = 'http://localhost:8080/health'
response = requests.get(url)
print(response)
print("All Systems On!!!" in response.text)
