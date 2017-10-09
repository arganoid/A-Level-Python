import random

def generate_one_time_pad(length):
    # the pad (key) is a random requence of characters (could in theory just use any number from 0-255)
    one_time_pad = []

    for i in range(0,length):
        chosen_char = chr( random.randint(ord('A'), ord('Z')) )  # randint is inclusive
        one_time_pad.append(chosen_char)

    return one_time_pad

def perform_vernam_encyrption(inputString, pad, reverse=False):
    # Output is a list of numbers rather than a string. This is because we are using the Unicode character set
    # rather than the Baudot code used in the textbook. In Baudot code almost every 5-bit code corresponds to
    # a letter, but in Unicode this is not the case - 0-31 are control characters with no visual representation
    outputList = []

    i = 0
    for i in range(0,len(inputString)):
        char = inputString[i]
        padChar = pad[i]
        charCode = ord(char)
        padCode = ord(padChar)

        charCodeXORpadCode = charCode ^ padCode  # ^ means perform bitwise XOR
        print("XOR {} {} = {} = {:0>8b}".format(charCode, padCode, charCodeXORpadCode, charCodeXORpadCode))
        charCode = charCodeXORpadCode

        outputList.append(charCode)

    return outputList

def perform_vernam_decryption(inputList, pad):
    outputString = ''

    i = 0
    for i in range(0,len(inputList)):
        inputCode = inputList[i]
        padCode = ord(pad[i])

        inputCodeXORpadCode = inputCode ^ padCode  # ^ means perform bitwise XOR

        outputString += chr(inputCodeXORpadCode)

    return outputString

####

plainText = 'This is a message to be passed through a Vernam (one time pad) cipher'

pad = generate_one_time_pad(len(plainText))

plainText = plainText.upper()
print('Original string: ' + plainText)

encrypted = perform_vernam_encyrption(plainText, pad)

encrypted_oneline = ''
for n in encrypted:
    encrypted_oneline += str(n) + ' '
print('Encrypted number sequence: ' + encrypted_oneline)

decryptedString = perform_vernam_decryption(encrypted, pad)
print('Decrypted string: ' + decryptedString)
