"""
-e  Encrypt
-d  Decrypt
-f  file name
-s  string


keyword.py -e -s "MESSAGE TO ENCRYPT" -k "gcse"

"""

import argparse

#alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-+=/*!\"£$%^&(){}[]'@#~,.<>/?\|¬`:;"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#alphabet = " !\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

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
    #Reverse operation for encryption, take letter values off each other to get message
    for m, k in zip(message, keyword):
        try:
            val = int((alphabet.index(m.upper()) + 1) - int(alphabet.index(k.upper()) + 1)) % len(alphabet)
        #Handle spaces
        except(ValueError):
            val = " "
        letterVals.append(val)
    #Construct decrypted message
    newMsg = ""
    for i in letterVals:
        try:
            newMsg += alphabet[i - 1]
        #Handle spaces
        except(TypeError):
            newMsg += " "
    return newMsg

def encryptFile(keyword, file):
    encLines = []
    with open(file, "r") as f:
        data = f.readlines()
        dataStr = ""
        for i in data:
            dataStr += i + "\n"
        print(keyword)
        encData = encrypt(dataStr, keyword)
        print(encData)
    with open("out.txt", "w") as g:
        g.write(encData)

def decryptFile(keyword, file):
    decLines = []
    with open(file, "r") as f:
        data = f.read()
        print(keyword)
        decData = decrypt(data, keyword)
        print(decData)
    with open("decfile.txt", "w") as g:
        g.write(decData)

if __name__ == "__main__":
    #Set up CLI arguments
    parser = argparse.ArgumentParser(description="Encrypt or decrypt text or a file.")
    #Mutually exclusive group for toggle flag for encryption or decryption
    encDec = parser.add_mutually_exclusive_group()
    encDec.add_argument("-e", action="store_true", dest="enc", default="store_true", help="Encrypt a string or file.")
    encDec.add_argument("-d", action="store_false", dest="enc", default="store_true", help="Decrypt a string or file.")
    #Keyword is always needed
    parser.add_argument("--keyword", "-k", action="store", help="Specifies the keyword to encrypt the message with")
    #Mutually exclusive group for either encrypting files or strings.
    fileStr = parser.add_mutually_exclusive_group()
    fileStr.add_argument("--filename", "-f", action="store", help="Specifies the name of the file to encrypt or decrypt")
    fileStr.add_argument("--string", "-s", action="store", help="Specifies the string to encrypt or decrypt")

    args = parser.parse_args()
    #print(args)
    if(args.enc):
        if(args.filename != None):
            #print(args.filename)#FILE ENC
            encryptFile(args.keyword, args.filename)
            print("File " + args.filename + " encrypted to out.txt")
        else:
            #print(args.string)#STRING ENC
            msg = encrypt(args.string, args.keyword)
            print(msg)
    else:
        print("enc is false")#SRING + FILE DEC
        if(args.filename == True):
            #print(args.string)#STRING ENC
            msg = decrypt(args.string, args.keyword)
            print(msg)
        else:
            #print(args.filename)#FILE ENC
            decryptFile(args.keyword, args.filename)
            print("File " + args.filename + " decrypted to decfile.txt")
    """
    msg = encrypt("SECRET MESSIG VERY CONFIDENTIAL", "gcse" + "wowee")
    print(msg)
    dec = decrypt(msg, "gcse" + "wowee")
    print(dec)
    
    encryptFile("gcse", "text.txt")
    decryptFile("gcse", "out.txt")"""
