def encrypt ( text , key ):
    result = ""
    text = text.lower()

    for i in range (len(text)):
        char = text[i]
        if (char != " "):
            result += chr((ord(char) + key - 97) % 26 + 97)
        else:
            result += " "
    return result

def decrypt ( text , key ):
    return encrypt(text, -key)

print(encrypt("Lorem ipsum", 5))
print(decrypt("qtwjr nuxzr", 5))