import bs4,requests, re, os

path = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(path,"xkcd"), exist_ok=True)
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "xkcd")

url = "https://xkcd.com/"
for i in range(10):
    print("Getting Page #%d"%(i+1))
    page = requests.get(url)
    page.raise_for_status()
    soup = bs4.BeautifulSoup(page.text, "html.parser")
    imgUrl = "http:" + soup.select("#comic img")[0].get("src")

    print("Getting Image #%d"%(i+1))
    print(imgUrl)
    imgReq = requests.get(imgUrl, headers={"Connection": "close"})
    print("Finished Getting Image")
    regex = "^.*/"
    imgFile = open(os.path.join(path, re.sub(regex,"",imgUrl)), "wb")
    for chunk in imgReq.iter_content(10**10):
        imgFile.write(chunk)

    imgFile.close()
    prev = soup.select_one('a[rel="prev"]')
    url = "https://xkcd.com" + prev.get("href")
    print("Finished Page #%d"%(i+1))

print("\nFinished")