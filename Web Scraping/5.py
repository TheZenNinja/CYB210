#????

fileOut = open("path", "wb")

for chunk in req.iter_content(10240):
    fileOut.write(chunk)