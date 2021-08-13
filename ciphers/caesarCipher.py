def encrypt ( text , key ):
    result = ""
    text = text.lower()

    for i in range (len(text)):
        char = text[i]

        result += chr((ord(char) + key - 97) % 26 + 97)
    return result

print(encrypt( "abcdefghijklmnoprstuwxyz" , 5 ))