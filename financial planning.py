#Financial Planning

def calculate_future_value(pv, r, n):
    """
    Function to calculate the future value of an investment.
    
    Parameters:
    pv (float): The present value or initial investment amount.
    r (float): The annual interest rate (as a decimal).
    n (int): The number of years the money is invested for.
    
    Returns:
    float: The future value of the investment.
    """
    fv = pv * (1 + r) ** n
    return fv

def calculate_gst(amount, gst_rate):
    """
    Function to calculate the GST (Goods and Services Tax) on a given amount.
    
    Parameters:
    amount (float): The original amount before GST.
    gst_rate (float): The GST rate (as a decimal).
    
    Returns:
    float: The total amount including GST.
    """
    gst_amount = amount * gst_rate
    total_amount = amount + gst_amount
    return total_amount

def calculate_shares_investment(investment,facevalue, marketvalue, shares):
    """
    Function to calculate the total value of shares investment.

    Parameters:
    investment (float): The total amount invested in shares.
    facevalue (float): The face value of a single share.
    marketvalue (float): The current market value of a single share.
    shares (int): The number of shares purchased.

    Returns:
            float: The total value of the shares investment.
    """
    total_value = shares * marketvalue
    return total_value

print("Welcome to the Financial Planning Calculator!")
print("Choose an option:")
print("1. Calculate future value of an investment")
print("2. Calculate GST on an amount")
print("3. Calculate total value of shares investment")
while True:
    choice = input("Enter your choice (1-3) or 'q' to quit: ")

    if choice == 'q':
        print("Exiting the calculator. Goodbye!")
        break

    if choice in ['1', '2', '3']:
        if choice == '1':
            pv = float(input("Enter the present value (initial investment): "))
            r = float(input("Enter the annual interest rate (as a decimal): "))
            n = int(input("Enter the number of years: "))
            result = calculate_future_value(pv, r, n)
            print(f"The future value of the investment is: {result}")

        elif choice == '2':
            amount = float(input("Enter the original amount before GST: "))
            gst_rate = float(input("Enter the GST rate (as a decimal): "))
            result = calculate_gst(amount, gst_rate)
            print(f"The total amount including GST is: {result}")

        elif choice == '3':
            investment = float(input("Enter the total amount invested in shares: "))
            facevalue = float(input("Enter the face value of a single share: "))
            marketvalue = float(input("Enter the current market value of a single share: "))
            shares = int(input("Enter the number of shares purchased: "))
            result = calculate_shares_investment(investment, facevalue, marketvalue, shares)
            print(f"The total value of the shares investment is: {result}")