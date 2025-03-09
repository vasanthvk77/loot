import requests

url = "https://loot-v6zf.onrender.com/api/songs/"
response = requests.get(url)

print("Status Code:", response.status_code)
print("Response Text:", response.text)
