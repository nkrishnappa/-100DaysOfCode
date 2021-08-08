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

#TODO-3.1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(choice: str, text: str, shift: int) -> None:
    converted_text = ""
    shift %= 26
    for letter in text:
        #TODO-4.3: What happens if the user enters a number/symbol/space?
        # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        # e.g. start_text = "meet me at 3"
        # end_text = "•••• •• •• 3"
        if letter.isalpha():
            position = alphabet.index(letter)
            if choice == "encode":
                index = position + shift
            elif choice == "decode":
                index = position - shift
            converted_text += alphabet[index]
        else:
            converted_text += letter
    print(f"The {choice}ed text is {converted_text}")

#TODO-4.1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

#TODO-4.4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

exit_flag = "yes"

#TODO-2.3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
while exit_flag == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #TODO-3.2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
    caesar(choice=direction, text=text, shift=shift)
    # if direction == "encode":
    #     #TODO-1.3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
    #     encrypt(text=text, shift=shift)
    # elif direction == "decode":
    #     decrypt(text=text, shift=shift)
    # else:
    #     print(f"invalid input : {direction}")
    exit_flag = input("Type 'yes' if you want to go again. Otherwise type no.\n")

print("Goodbye.")