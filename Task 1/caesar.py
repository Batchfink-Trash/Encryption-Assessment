from collections import deque

alphabet = deque("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def encrypt(message, offset):
    string = ""
    indexes = []
    #Loop through the message, and log positions of chars in alphabet deque. Handle spaces separately
    for i in message:
        try:
            indexes.append(alphabet.index(i.upper()))
        except ValueError:
            indexes.append(" ")
    #Rotate deque to the left by specified amount
    alphabet.rotate(0 - offset)
    #Build message from indexes and rotated deque (handing spaces accordingly)
    for j in indexes:
        try:
            string += alphabet[j]
        except TypeError:
            string += " "
    alphabet.rotate(offset)
    return string

def decrypt(message, offset):
    return encrypt(message, (0 - offset))
    
if __name__ == "__main__":
    print(encrypt("COMPUTING IS FUN", 5))   #HTRUZYNSL NX KZS
    print(decrypt("HTRUZYNSL NX KZS", 5))
    
    operation = input("Encrypt or decrypt a message? (e/d): ")
    
    if operation == "e":
        msg = input("Enter a message to encrypt (just letters please): ")
        offs = int(input("What should the offset be?: "))
        print(encrypt(msg, offs))
    else:
        msg = input("Enter the message to decrypt (just letters please): ")
        offs = int(input("What is the offset?: "))
        print(encrypt(msg, offs))