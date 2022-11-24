import re


def e_ceaser_cipher(message, key):
    res = ""

    for c in message:
        if c.isupper():
            # ord() function returns the Unicode code from a given character
            res += chr((ord(c) + key - 65) % 26 + 65)
        elif c.islower():
            # chr() method returns a string representing a character whose Unicode code point is an integer.
            res += chr((ord(c) + key - 97) % 26 + 97)
        elif c == " ":
            res += " "
        elif(c.isdigit()):
            res += str((int(c)+key) % 10)
        else:
            res += c
    return res


def decryption(cipher_txt, key):
    result = ""

    for c in cipher_txt:
        if c.isupper():
            x = chr((int(ord(c)) - 65 - key) % 26 + 65)
            result += x

        elif c.islower():
            x = chr((int(ord(c)) - 97 - key) % 26 + 97)
            result += x

        elif c.isdigit():
            x = (int(c) - key) % 10
            result += str(x)
        else:
            result += c
    return result


if __name__ == "__main__":
    message = input("Enter Your message : ")
    key = int(input("Enter Key: "))
    result = e_ceaser_cipher(message, key)
    print(f"Your encripted message is : {result}")
    print(f"message was : {decryption(result, key)}")

    dec_text = input("enter decrypted message ")
    key = int(input("enter key "))
    print("Message is : " + decryption(dec_text, key))
