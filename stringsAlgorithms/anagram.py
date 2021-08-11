def isAnagram ( word1 , word2 ):
    word1 = word1.lower()
    word2 = word2.lower()
    if len( word1 ) != len( word2 ):
        return False
    sortedFirstWord = sorted( word1 )
    sortedSecondWord = sorted( word2 )

    for i in range( 0 , len(word1) ):
        if sortedFirstWord[i] != sortedSecondWord[i]:
            return False
    return True

print(isAnagram( "adam" , "dama" ))
print(isAnagram("word1","word2"))
print(isAnagram("Lenin","ninle"))