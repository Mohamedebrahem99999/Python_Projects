import string
ALPHABET = string.ascii_lowercase
ALPHABET_DICT = {ch: i for i, ch in enumerate(ALPHABET)}

def get_shift(user_shift):
    while True:
        try:
            return int(user_shift)
        except ValueError:
            print("Shift must be a number")
            user_shift = input("Enter a numeric shift")

def encrypt(message,shift):
    encrypted_word = []

    for letter in message:
        if letter.lower() in ALPHABET_DICT:
            index = ALPHABET_DICT[letter.lower()]
            encrypted_letter = ALPHABET[(shift + index) % 26]
            encrypted_word.append(encrypted_letter.upper() if letter.isupper() else encrypted_letter)
        else:
            encrypted_word.append(letter)

    return "".join(encrypted_word)

def decrypt(message, shift):
    return encrypt(message, -shift)
def main():

    shift = get_shift(input("Enter the shift: "))
    message = input("Enter the original message: ")
    choice = input("Do you want to (encrypt or decrypt) the message?").lower()
    while choice not in ["encrypt","decrypt"]:
        choice = input("Please input (encrypt or decrypt)").lower()

    print(encrypt(message, shift) if choice == "encrypt"
          else decrypt(message,shift))
main()