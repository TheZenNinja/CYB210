def railEncrypt(plainTxt, railNum):
    rails = []
    for i in range(railNum):
        rails.append("");

        pos = 0
        for c in plainTxt:
            if pos >= railNum:
                pos = 0;
            rails[pos] += c;
            pos += 1
        while pos < railNum:
            rails[pos] += " ";
            pos += 1

        return "".join(rails)

def railDecrypt(cipherTxt, railNum):
    railLen = len(cipherTxt)//railNum
    plainTxt = ""
    for col in range(railLen):
        for rail in range(railNum):
            nextletter = col + rail * railLen;
            plainTxt += cipherTxt[nextLetter]
    return plainTxt


