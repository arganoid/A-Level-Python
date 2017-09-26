def perform_caesar_encyrption(inputString, shift):
    outputString = ''

    for char in inputString:
        # ??
        outputString += char

    return outputString

####

originalString = 'This is a message'
originalString = originalString.upper()
print('Original string: ' + originalString)

encrypted = perform_caesar_encyrption(originalString, 5)
print('Encrypted string: ' + encrypted)

decrypted = perform_caesar_encyrption(encrypted, -5)
print('Decrypted string: ' + decrypted)
