import re

url = "https://cheatography.com/davechild/cheat-sheets/regular-expressions/"
regex = "(^https://)|(/.*)"

print(re.sub(regex,"",url))