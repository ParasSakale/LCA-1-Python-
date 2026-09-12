#Python program to check that a string contains only a certain set of characters
# (in this case a-z, A-Z and 0-9).

print("=" * 50)
print("Welcome to the String checker")
print("=" * 50)


while True:
    input_string = input("Type your string : ")

    is_valid = True
    for character in input_string:
        if not character.isalnum():
            is_valid = False
            break

    if is_valid:
        print("The string contains only characters (a-z , A-Z) and digits (0-9)")
        print("Hence it is a string")
    else:
        print("The string contains characters outside a-z, A-Z, 0-9")
        print("Hence it is not a string")

    check_another_string = input("Want to check for another string (y/n) : ")
    if check_another_string != "y":
        print("=" * 50)
        print("Thank you for using this program")
        print("=" * 50)
        break
