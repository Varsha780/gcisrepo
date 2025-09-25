def triangle_validator(side1, side2, side3):
    # Check for triangle inequality
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        return True
    else:
        return False


def triangle_type(side1, side2, side3):
    if side1 == side2 == side3:
        print("This is an equilateral triangle.")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("This is an isosceles triangle.")
    else:
        print("This is a scalene triangle.")


def main():
    side1 = float(input("Enter the length of side A: "))
    side2 = float(input("Enter the length of side B: "))
    side3 = float(input("Enter the length of side C: "))

    if triangle_validator(side1, side2, side3):
        triangle_type(side1, side2, side3)
    else:
        print("The entered sides do not form a valid triangle.")


main()
