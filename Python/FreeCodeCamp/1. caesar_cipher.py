def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int): #Si no es un entero
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25: #Si no esta entre 1 y 25
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz' 

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    print("shifted_alphabet:", shifted_alphabet)
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    print("Translation Table:", translation_table)  
    encrypted_text = text.translate(translation_table)
    print("Encrypted Text:", encrypted_text)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

#encrypted_text = encrypt('freeCodeCamp', 3)
encrypted_text = 'iuhhFrghFdps'
dencrypted_text = decrypt(encrypted_text, 3)
