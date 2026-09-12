# Python program to find the largest of three numbers

#Fancy details
print("=" * 50)
print("Let's find the largest number among three!")
print("=" * 50)

#Actual code
while True:
    num1 = float(input("Enter your 1st number : "))
    num2 = float(input("Enter your 2nd number : "))
    num3 = float(input("Enter your 3rd number : "))

    if num1 > num2 and num1 > num3:
        print("1st number is the largest")
    elif num2 > num1 and num2 > num3:
        print("2nd number is the largest")
    else:
        print("3rd number is the largest")
    play_again = input("Do you want to check again for other 3 numbers(y/n):")
    if play_again != "y":
        print("=" * 50)
        print("Thank you for using this program")
        print("=" * 50)
        break