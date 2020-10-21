def vignereEncrypt(string, key): 
    string = string.capitalize()
    key = key.capitalize()
    cipherTxt = "" 
    keystream = ""
    while len(keystream) < len(string):
        keystream += key;

    for i in range(len(string)):
        if (string[i] == " "):
            cipherTxt += " "
        else:
            x = (ord(string[i]) + ord(keystream[i])) % 26
            x += 65 
            print("")
            

            cipherTxt += chr(x) 
    return(cipherTxt) 

file = open("passwords-plainText.txt", "r")
passwords = []

key = "HelloWorld"

for line in file:
    passwords.append(vignereEncrypt(line, key) + "\n")

file.close()

newFile = open("passwords-encrypted.txt", "w")
newFile.writelines(passwords)
newFile.close()