def isPalindrome( string ):
    size = len( string )
    string = string.lower()
    revertedString = ""
    for i in range(size-1, -1, -1):
      revertedString+=string[i]
    if string == revertedString:
        return True
    else:
        return False



print(isPalindrome( "Kayak" ))
print(isPalindrome("Lewd did I live & evil I did dwel"))
print(isPalindrome("madam"))
print(isPalindrome("Marxism-Leninism"))