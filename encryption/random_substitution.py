import random

def dictionary_key_value_swap(input_dictionary):
    output_dictionary = {}
    for key, value in input_dictionary.items():
        output_dictionary[value] = key
    return output_dictionary

def generate_random_substitution_table():
    substitution_table = {}  # {} = create empty dictionary

    letters = []
    for i in range(0,26):
        letters.append( chr(i + ord('A')))

    for char_code in range(ord('A'),ord('Z') + 1):
        chosen_index = random.randint(0, len(letters) - 1)  # randint is inclusive
        substitution_table[chr(char_code)] = letters[chosen_index]
        del letters[chosen_index]

    print(substitution_table)

    return substitution_table

def perform_random_substitution_encyrption(inputString, substitution_table):
    outputString = ''

    for char in inputString:
        charCode = ord(char)
        if charCode >= ord('A') and charCode <= ord('Z'):
            outputString += substitution_table[char]
        else:
            outputString += char

    return outputString

####

substitution_table = generate_random_substitution_table()

originalString = 'This is a message to be passed through a random substitution cipher'
originalString = originalString.upper()
print('Original string: ' + originalString)

encrypted = perform_random_substitution_encyrption(originalString, substitution_table)
print('Encrypted string: ' + encrypted)

reverse_substitution_table = dictionary_key_value_swap(substitution_table)
decrypted = perform_random_substitution_encyrption(encrypted, reverse_substitution_table)
print('Decrypted string: ' + decrypted)
