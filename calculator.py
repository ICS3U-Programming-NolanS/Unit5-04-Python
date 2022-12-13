#!/usr/bin/env python3

# Created by: Nolan Shami
# Created on: Dec 13th, 2022
# This program asks the user for three parameters
# the parameters are an operation and two numbers
# and then it calculates and displays the results


# Function which performs the calculations
def calculate(sign, first_num, second_num):

    # If the sign is division, divide the numbers
    if sign == "/":
        result = first_num / second_num
    # If the sign is multiplication, multiply the numbers
    elif sign == "*":
        result = first_num * second_num
    # If the sign is modulus, get the remainder
    elif sign == "%":
        result = first_num % second_num
    # If the sign is addition, add the numbers
    elif sign == "+":
        result = first_num + second_num
    # Otherwise it must be subtraction, so subtract the numbers
    else:
        result = first_num - second_num
    # Return the result of the calculation
    return result


# Main function to get the numbers and operation
def main():
    # Explain what the program does
    print("This program performs calculations between two numbers!")
    print("")

    # Get the users operation of choice
    sign_user = input(
        "Enter what operation you would like to perform (-, *, %, /, +): "
    )

    # Check if invalid operator was entered
    if (
        sign_user == "-"
        or sign_user == "%"
        or sign_user == "*"
        or sign_user == "/"
        or sign_user == "+"
    ):
        # Get the users first number
        first_num_string = input("Enter the first number: ")

        try:
            # Convert the first number to a float
            first_num_float = float(first_num_string)

            # Get the users first number
            second_num_string = input("Enter the second number: ")

            try:
                # Convert the second number to a float
                second_num_float = float(second_num_string)
                # Assign the returned value to this variable
                result_user = calculate(sign_user, first_num_float, second_num_float)
                # Display the result of the calculations
                print(
                    "The result of {} {} {} is {}".format(
                        first_num_float, sign_user, second_num_float, result_user
                    )
                )
            # Catches invalid number input
            except Exception:
                print("{} is an invalid number.".format(second_num_string))
        # Catches invalid number input
        except Exception:
            print("{} is an invalid number.".format(first_num_string))
    else:
        # Catches invalid operator input
        print("It seems that {} is not a recognizable operation.".format(sign_user))


if __name__ == "__main__":
    main()
