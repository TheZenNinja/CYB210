import goslate;
import random;
#goslate is too slow
languages = []
currentLang = ""
prevLang = ""
gs = goslate.Goslate(writing=goslate.WRITING_ROMAN)
languages= list(gs.get_languages().keys())

inputTxt = "Hello" #input("Type text to be randomized: ")
outputTxt = inputTxt
for i in range(100):
    print(i)
    while (prevLang == "") or (currentLang == prevLang):
        currentLang = languages[random.randint(0,len(languages)-1)]

    outputTxt = gs.translate(outputTxt, currentLang)

print(outputTxt)
