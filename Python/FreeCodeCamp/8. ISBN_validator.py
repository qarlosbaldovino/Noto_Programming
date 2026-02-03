def validate_isbn(isbn, length):
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return

    main_digits = isbn[:length - 1] #080442957
    if length == 10 and isbn[length - 1] == 'X':
        given_check_digit = '10' # X = 10
    else:
        given_check_digit = isbn[length - 1] #X

    if not main_digits.isdigit() or not given_check_digit.isdigit():
        print('Invalid character was found.')
        return

    main_digits_list = [int(digit) for digit in main_digits] #[0,8,0,4,4,2,9,5,7]

    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)

    if int(given_check_digit) == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')

def calculate_check_digit_10(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        digits_sum += (index+1) * digit
    return digits_sum % 11

def calculate_check_digit_13(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list, 1):
        if index % 2 == 0:
            digits_sum += (digit * 3)
        else:
            digits_sum += (digit * 1)
    return (10 - (digits_sum % 10)) % 10

def main():
    user_input = '080442957X,10'
    #user_input = input('Enter ISBN and length: ')

    try:
        values = user_input.split(',')
        isbn = values[0]
        length = int(values[1])
    except IndexError:
        print("Enter comma-separated values.")
        return
    except ValueError:
        print("Length must be a number.")
        return
  
    if length == 10 or length == 13:
            validate_isbn(isbn, length)
    else:
            print('Length should be 10 or 13.')

main()