indexVal = 0
Ciphertext = ""
text = input("Please enter in a messege to encrypt: ")

CipherKey = int(input("Enter Key: "))

for indexVal in range(0, len(text)):
    singleChar = text[indexVal].upper()
    
    if singleChar >= 'A' and singleChar <= 'Z':
        singleChar = chr(ord(singleChar) + CipherKey)

        if singleChar > 'Z':
            singleChar = chr(ord(singleChar) - 26)

    Ciphertext = Ciphertext + singleChar

print(Ciphertext)
input('Press ENTER to exit')