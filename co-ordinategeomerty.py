#CO-ORDINATE GEOMETRY

def distance(x1, y1, x2, y2):
    """Calculate the distance between two points (x1, y1) and (x2, y2) in 2D space."""
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
    print("Distance between points is:", distance)

def midpoint(x1, y1, x2, y2):
    """Calculate the midpoint between two points (x1, y1) and (x2, y2) in 2D space."""
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    return (mid_x, mid_y)
    print("Midpoint between points is:", midpoint)

def slope(x1, y1, x2, y2):
        """Calculate the slope of the line passing through two points (x1, y1) and (x2, y2)."""
        if x2 - x1 == 0:
            return None  # Slope is undefined for vertical lines
        return (y2 - y1) / (x2 - x1)
        print("Slope of the line is:", slope)

def equation_of_line(x1, y1, x2, y2):
    """Calculate the equation of the line passing through two points (x1, y1) and (x2, y2)."""
    m = slope(x1, y1, x2, y2)
    if m is None:
        return f"x = {x1}"  # Vertical line
    b = y1 - m * x1
    return f"y = {m}x + {b}"
    print("Equation of the line is:", equation_of_line)


def area_of_triangle(x1, y1, x2, y2, x3, y3):
    """Calculate the area of a triangle formed by three points (x1, y1), (x2, y2), and (x3, y3) in 2D space."""
    return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2)
    print("Area of the triangle is:", area_of_triangle)


def is_collinear(x1, y1, x2, y2, x3, y3):
    """Check if three points (x1, y1), (x2, y2), and (x3, y3) are collinear."""
    return (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1)
    print("Are the points collinear?", is_collinear)


print("Welcome to the Co-ordinate Geometry Calculator!")
print("Choose an option:")
print("1. Calculate distance between two points")
print("2. Calculate midpoint between two points")
print("3. Calculate slope of the line passing through two points")
print("4. Calculate equation of the line passing through two points")
print("5. Calculate area of a triangle formed by three points")
print("6. Check if three points are collinear")

while True:
    choice = input("Enter your choice (1-6) or 'q' to quit: ")

    if choice == 'q':
        print("Exiting the calculator. Goodbye!")
        break

    if choice in ['1', '2', '3', '4', '5', '6']:
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))

        if choice == '1':
            result = distance(x1, y1, x2, y2)
            print(f"Distance between points is: {result}")

        elif choice == '2':
            result = midpoint(x1, y1, x2, y2)
            print(f"Midpoint between points is: {result}")

        elif choice == '3':
            result = slope(x1, y1, x2, y2)
            if result is None:
                print("Slope of the line is undefined (vertical line).")
            else:
                print(f"Slope of the line is: {result}")

        elif choice == '4':
            result = equation_of_line(x1, y1, x2, y2)
            print(f"Equation of the line is: {result}")

        elif choice == '5':
            x3 = float(input("Enter x3: "))
            y3 = float(input("Enter y3: "))
            result = area_of_triangle(x1, y1, x2, y2, x3, y3)
            print(f"Area of the triangle is: {result}")

        elif choice == '6':
            x3 = float(input("Enter x3: "))
            y3 = float(input("Enter y3: "))
            result = is_collinear(x1, y1, x2, y2, x3, y3)
            if result:
                print("The points are collinear.")
            else:
                print("The points are not collinear.")

    else:
        print("Invalid choice. Please try again.")