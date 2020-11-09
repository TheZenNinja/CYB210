import requests

req = requests.get("http://inventwithpython.com/")
req.raise_for_status()
fileOut = open("5 Output.txt", "wb")

for chunk in req.iter_content(100000):
    fileOut.write(chunk)

fileOut.close()
print("Done")