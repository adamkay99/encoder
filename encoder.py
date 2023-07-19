#Adam Kay
def encode(password):
    encoded_password = ""
    for i in password:
        if int(i) > 6:
            encoded_password += str(int(i) - 7)
        else:
            encoded_password += str(int(i) + 3)
    print("Your password has been encoded and stored!\n")
    return int(encoded_password)


def decode(encoded_password):
    encoded_password = str(encoded_password)
    decoded_password = ''
    for i in encoded_password:
        if int(i) - 3 < 0:
            decoded_password += str(int(i) - 3 + 10)
        else:
            decoded_password += str(int(i) - 3)
    return decoded_password


if __name__ == "__main__":
    while True:
        print("Menu"
              "\n-------------"
              "\n1. Encode"
              "\n2. Decode"
              "\n3. Quit")
        selection = int(input("\nPlease enter an option: "))
        if selection == 1:
            to_be_encoded = input("Please enter your password to encode: ")
            encoded_password = encode(to_be_encoded)
        elif selection == 2:
            print(f"The encoded password is {encoded_password}"
                  f", and the original password is {decode(encoded_password)}\n")
        elif selection == 3:
            exit()
