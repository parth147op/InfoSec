def getKey(str, key):
    key = list(key)
    if (len(str) == len(key)):
        return ("".join(key))
    else:
        for i in range(len(str) - len(key)):
            key.append(key[i % len(key)])
    return ("".join(key))

def encryptText(str, key):
    cipher = []
    for i in range(len(str)):
        x = (ord(str[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher.append(chr(x))
    return ("".join(cipher))

def decryptCipher(str, key):
    normalText = []
    for i in range(len(str)):
        x = (ord(str[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        normalText.append(chr(x))
    return ("".join(normalText))


if __name__ == "__main__":
        inputText = input("Enter Message: ")
        inputKey = input("Enter Key: ")
        key = getKey(inputText, inputKey.upper())
        encryptedText = encryptText(inputText.upper(), key)
        print(f"Cipher Text: {encryptedText}")
        decryptedCipher = decryptCipher(encryptedText, key)
        print(f"Plain Text: {decryptedCipher}")
