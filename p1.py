def run_program(choice):
    if choice == 1:
        # Largest of two numbers
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        if a > b:
            print("The largest number is", a)
        else:
            print("The largest number is", b)
    
    elif choice == 2:
        # Largest of three numbers
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        c = int(input("Enter third number: "))
        if a > b and a > c:
            print("Largest number is", a)
        elif b > a and b > c:
            print("Largest number is", b)
        else:
            print("Largest number is", c)
    
    elif choice == 3:
        # Check if even or odd
        a = int(input("Enter first number: "))
        if a % 2 == 0:
            print("This is an even number")
        else:
            print("This is an odd number")
    
    elif choice == 4:
        # Check if divisible by 10
        a = int(input("Enter first number: "))
        if a % 10 == 0:
            print("Divisible by 10")
        else:
            print("Not divisible by 10")
    
    elif choice == 5:
        # Check if minor or major
        age = int(input("Enter age: "))
        if age < 18:
            print("The person is minor")
        else:
            print("The person is major")
    
    elif choice == 6:
        # Length of input string
        a = input("Enter a number: ")
        print(len(a))
    
    elif choice == 7:
        # Leap year check
        year = int(input("Enter a year: "))
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print("Year is leap year")
        else:
            print("Year is not leap year")
    
    elif choice == 8:
        # Triangle validity
        a = int(input("Enter first angle: "))
        b = int(input("Enter second angle: "))
        c = int(input("Enter third angle: "))
        total = a + b + c
        if total == 180:
            print("This is a valid triangle")
        else:
            print("This is not a valid triangle")
    
    elif choice == 9:
        # Absolute value
        a = int(input("Enter first number: "))
        if a < 0:
            print(-a)
        else:
            print(a)
    
    elif choice == 10:
        # Compare area and perimeter of rectangle
        length = int(input("Enter length: "))
        breadth = int(input("Enter breadth: "))
        area = length * breadth
        perimeter = 2 * (length + breadth)
        if area > perimeter:
            print("Area is greater")
        else:
            print("Perimeter is greater")
    
    elif choice == 11:
        # Check if points are collinear
        x1 = int(input("Enter first point (x1): "))
        y1 = int(input("Enter second point (y1): "))
        x2 = int(input("Enter third point (x2): "))
        y2 = int(input("Enter fourth point (y2): "))
        x3 = int(input("Enter fifth point (x3): "))
        y3 = int(input("Enter sixth point (y3): "))
        area_of_triangle = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
        if area_of_triangle == 0:
            print("All points are on the same line")
        else:
            print("All points are not on the same line")
    
    else:
        print("Invalid choice. Please select a number between 1 and 11.")

# Main menu to select which program to run
print("Select a program to run:")
print("1. Largest of two numbers")
print("2. Largest of three numbers")
print("3. Check if even or odd")
print("4. Check if divisible by 10")
print("5. Check if minor or major")
print("6. Length of input string")
print("7. Leap year check")
print("8. Triangle validity")
print("9. Absolute value")
print("10. Compare area and perimeter of rectangle")
print("11. Check if points are collinear")

choice = int(input("Enter your choice (1-11): "))
run_program(choice)