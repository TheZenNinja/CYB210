import urllib.request as req
def SavePage(url):
    page = req.urlopen(url)
    file = open("Saved Website.txt", "w")
    line = page.readline().decode("utf-8")
    while line != "":
        file.write(line + "\n")
        line = page.readline().decode("utf-8")
    file.close()

SavePage("http://help.websiteos.com/websiteos/example_of_a_simple_html_page.htm")