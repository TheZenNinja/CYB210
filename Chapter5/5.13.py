import urllib.request as req
def SavePage(fileName, url):
    page = req.urlopen(url)
    file = open((fileName + ".txt"), "w")
    line = page.readline().decode("utf-8")
    while line != "":
        file.write(line + "\n")
        line = page.readline().decode("utf-8")
    file.close()
    print("Finished")

SavePage("Saved Site", "http://help.websiteos.com/websiteos/example_of_a_simple_html_page.htm")