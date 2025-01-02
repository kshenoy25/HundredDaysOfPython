from asyncio import create_eager_task_factory

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]

    print(f"Here is the encoded result: {cipher_text}")

def decrypt(original_text, shift_amount):
    output_text = ""

    for letter in original_text:
        # position of the new letter
        # current letter - shift amount
        shifted_position = alphabet.index(letter) - shift_amount

        # divide by the length of the alphabet(will never go out of range of this length)
        shifted_position %= len(alphabet)

        # adding it to the cipher text
        output_text += alphabet[shifted_position]

    print(f"Here is the decoded result: {output_text}")

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter

        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode} result: {output_text}")



#encrypt(original_text=text, shift_amount=shift)
#decrypt(original_text=text, shift_amount=shift)

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)


restart = input("Do you want to play again?(y/n)\n").lower()
if restart == "n":
    should_continue = False
    print("Thank you for playing! GoodBye.")
