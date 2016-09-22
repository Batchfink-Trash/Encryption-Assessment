alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#   --- Match keyword length with message length ---    #
def prepKeywd(message, keyword):
    keyWdProg = 0
    newKeyWd = ""
    for i in range(0, len(message)):
        keyIndex = i % len(keyword)     #modulo divides i by the keyword length then returns the remainder.  
        newKeyWd += keyword[keyIndex]   #eg. if i was 14 and len(keyword) was 4, this would return 1.
    return newKeyWd                     #This 'loops' the keyword to match the message length. eg. 'gcsegcsegc'

#   --- Encrypt message ---   #
def encrypt(message, keyword):
    keyword = prepKeywd(message, keyword)
    totalVals = []
    #Loop through both the message and keyword, adding the alphabet values of each letter together, and then to an array.
    for m, k in zip(message, keyword):
        try:
            val = int((alphabet.index(m.upper()) + 1) + (alphabet.index(k.upper()) + 1)) % len(alphabet)    #Use modulo again to wrap the alphabet around
        #Handle spaces in the message
        except(ValueError):
            val = " "
        totalVals.append(val)
    #Construct an encrypted string based on the values of the keyword and message values
    newMsg = ""
    for i in totalVals:
        try:
            newMsg += alphabet[i - 1]
        #Handle spaces
        except(TypeError):
            newMsg += " "
    return newMsg

def decrypt(message, keyword):
    keyword = prepKeywd(message, keyword)
    letterVals = []
    for m, k in zip(message, keyword):
        try:
            val = int((alphabet.index(m.upper()) + 1) - int(alphabet.index(k.upper()) + 1)) % len(alphabet)
        #Handle spaces
        except(ValueError):
            val = " "
        letterVals.append(val)
    newMsg = ""
    for i in letterVals:
        try:
            newMsg += alphabet[i - 1]
        #Handle spaces
        except(TypeError):
            newMsg += " "
    return newMsg

if __name__ == "__main__":
    msg = encrypt("computing is fun", "gcse")
    print(msg)
    dec = decrypt(msg, "gcse")
    print(dec)