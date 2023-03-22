
stored_encoded_password = ''


class LessThanEightError(Exception):
    pass


def encode_password(string_data):
    encoded_password = ''

    if len(string_data) < 8:
        raise LessThanEightError

    for character in string_data:
        encoded_password += str((int(character) + 3) % 10)

    return encoded_password


def decode_password(string_data):
	decoded_password = ''
	for digit in string_data:
		decoded_password += str((int(digit) + 7) % 10)
	return decoded_password


def menu():
    print('Menu\n'
          '-------------\n'
          '1. Encode\n'
          '2. Decode\n'
          '3. Quit\n')


if __name__ == '__main__':
    cont = True

    while cont:
        menu()
        try:
            user_input = int(input('Please enter an option: '))
            if user_input < 1 or user_input > 3:
                raise ValueError
        except ValueError:
            print('Error! Please enter a valid menu option!')
            continue

        try:
            if user_input == 1:
                password_input = input('Please enter your password to encode: ')
                stored_encoded_password = encode_password(password_input)
                print('Your password has been encoded and stored!\n')
            elif user_input == 2:
                stored_decoded_password = decode_password(stored_encoded_password)
                print('The encoded password is ', stored_encoded_password, ', and the original password is ', stored_decoded_password, '.', sep='')
            elif user_input == 3:
                cont = False

        except LessThanEightError:
            print('Error! Password must be 8 or more characters')
