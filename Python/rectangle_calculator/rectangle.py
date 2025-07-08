import calculator

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = calculator.area(length, width)
perimeter = calculator.perimeter(length, width)

print(f"The area of the rectangle is: {area}")
print(f"The perimeter of the rectangle is: {perimeter}")