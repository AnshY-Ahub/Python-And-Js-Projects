#ARITHMETIC PROGRESSION
def arithmetic_progression(a, d, n):
    """
    Function to calculate the nth term of an arithmetic progression.
    
    Parameters:
    a (int): The first term of the arithmetic progression.
    d (int): The common difference between consecutive terms.
    n (int): The term number to find.
    
    Returns:
    int: The nth term of the arithmetic progression.
    """
    nth_term = a + (n - 1) * d
    return nth_term

def sum_of_ap(a, d, n):
    """
    Function to calculate the sum of the first n terms of an arithmetic progression.
    
    Parameters:
    a (int): The first term of the arithmetic progression.
    d (int): The common difference between consecutive terms.
    n (int): The number of terms to sum.
    
    Returns:
    int: The sum of the first n terms of the arithmetic progression.
    """
    sum_ap = n * (2 * a + (n - 1) * d) / 2
    return sum_ap



print("Welcome to the Arithmetic Progression Calculator!")
print("Choose an option:")
print("1. Calculate the nth term of an arithmetic progression")
print("2. Calculate the sum of the first n terms of an arithmetic progression")

choice = input("Enter your choice (1-2) or 'q' to quit: ")

while True:
    if choice == 'q':
        print("Exiting the calculator. Goodbye!")
        break
    if choice in ['1', '2']:
        a = float(input("Enter the first term (a): "))
        d = float(input("Enter the common difference (d): "))
        n = int(input("Enter the term number (n): "))

        if choice == '1':
            result = arithmetic_progression(a, d, n)
            print(f"The {n}th term of the arithmetic progression is: {result}")

        elif choice == '2':
            result = sum_of_ap(a, d, n)
            print(f"The sum of the first {n} terms of the arithmetic progression is: {result}")