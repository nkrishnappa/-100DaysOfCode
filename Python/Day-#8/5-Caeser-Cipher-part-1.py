alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1.1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text: str, shift: int) -> None:
    #TODO-1.2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    cipher_text = ""
    for letter in text:
        encrypt_letter_index = (alphabet.index(letter) + shift) % 26
        cipher_text += alphabet[encrypt_letter_index]
    print(f"The enocoded text is {cipher_text}")

#TODO-2.1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text: str, shift: int) -> None:
    #TODO-2.2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
    decrypt_text = ""
    for letter in text:
        decrypt_letter_index = (alphabet.index(letter) - shift) % 26
        decrypt_text += alphabet[decrypt_letter_index]
    print(f"The decrypted text is {decrypt_text}")

#TODO-2.3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        #TODO-1.3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
        encrypt(text=text, shift=shift)
    elif direction == "decode":
        decrypt(text=text, shift=shift)
    else:
        print(f"invalid input : {direction}")
