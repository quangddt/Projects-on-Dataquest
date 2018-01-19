import requests

response = requests.get("https://api.github.com/users/quangddt/repos")

print(response.json())
