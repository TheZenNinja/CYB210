import requests

response = requests.get("http://inventwithpython.com/")

print("Download Succeeded" if response.status_code == 200 else "Download Failed")