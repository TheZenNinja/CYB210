def substitutionEncrypt(text,key):
	alphabet = "abcdefghijklmnopqrstuvwxyz "
	text = str(text).lower()
	cipher = ""
	for c in text:
			i = alphabet.find(c)
			cipher += key[i]
	return cipher;

def substitutionDecrypt(text,key):
	alphabet = "abcdefghijklmnopqrstuvwxyz "
	text = text.lower()
	plain = ""
	for c in text:
			i = key.find(c)
			plain += alphabet[i]
	return plain;

key = "qwertyuiopasdfghjklzxcvbnm "
text = "the quick brown fox jumps over the lazy dog";
encriptedText = substitutionEncrypt(text, key)
print(encriptedText)
print(substitutionDecrypt(encriptedText, key))