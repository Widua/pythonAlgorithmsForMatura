import re
def search ( toFind , text ):
    if re.search(toFind , text):
        match = re.search(toFind,text)
        print("Match at index %s, %s" % (match.start(), match.end() -1))

def isPhoneNumber( potentialNumber ):

    phoneRegex = r"([\+]?[0-9]{2})?[/ ]?([0-9][/ ]?){9}"

    if re.match( phoneRegex , potentialNumber ):
        return True
    else:
        return False

def isEmailAddress (potentialEmail):
    emailRegex = r"([\.]?[/-]?[\w]?)+[@][\w]*[.]+[\w]{2,4}"

    if re.match( emailRegex , potentialEmail ):
        return True
    else:
        return False

search( "toFind", "SoHardtoFindInThatString?" )
print(isPhoneNumber("333222111"))
print(isPhoneNumber("+44333222111"))
print(isPhoneNumber("+44 333222111"))
print(isPhoneNumber("333 222 111"))
print(isEmailAddress("mikolaj.widla@gmail.com"))
print(isEmailAddress("qq@@.com"))
