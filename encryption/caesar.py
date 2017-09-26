def perform_caesar_encyrption(inputString, shift):
    outputString = ''

    for char in inputString:
        charCode = ord(char)

        if charCode >= ord('A') and charCode <= ord('Z'):
            charCode += shift

            # change range to 0-25. % is mod (remainder)
            charCode -= ord('A')
            charCode %= 26

            # change range back to 'A' to 'Z'
            charCode += ord('A')

        outputString += chr(charCode)

    return outputString

####

originalString = 'This is a message to be passed through a Caesar cipher'
originalString = originalString.upper()
print('Original string: ' + originalString)

encrypted = perform_caesar_encyrption(originalString, 5)
print('Encrypted string: ' + encrypted)

decrypted = perform_caesar_encyrption(encrypted, -5)
print('Decrypted string: ' + decrypted)
