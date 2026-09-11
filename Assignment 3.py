# Python program to check whether or not the triangle is a right-angled triangle using function.

print("=" * 52)
print("Welcome to the Right Angled Triangle checker program")
print("=" * 52)

def right_angled_triangle(side_a = int, side_b = int, side_c = int):
    # Sort the sides so that the largest is treated as the potential hypotenuse
    sides = sorted([side_a, side_b, side_c])
    x, y, z = sides
    return x ** 2 + y ** 2 == z ** 2

while True:
    side_a = int(input("Enter the length of side a : "))
    side_b = int(input("Enter the length of side b : "))
    side_c = int(input("Enter the length of side c : "))

    if right_angled_triangle(side_a, side_b, side_c):
        print("It is a Right Angled Triangle")
    else:
        print("It is not a Right Angled Triangle")

    check_again = input("Want to check for other 3 sides (y/n) : ")

    if check_again != "y":
        print("=" * 50)
        print("Thank you for using this program")
        print("=" * 50)
        break

