import requests
# GET → Get data
response = requests.get(
    "https://jsonplaceholder.typicode.com/users/1"
)                                                         

print("Status:", response.status_code)

data = response.json()                  # JSON → Python
print("Username:", data["username"])

# POST → Send data
new_user = {"username": "abc"}

response = requests.post(
    "https://jsonplaceholder.typicode.com/users",
    json=new_user
)

print("POST Status:", response.status_code)
print("Response:", response.json())