# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main() : 
    savings_balance = float(input("Enter savings account balance: "))
    savings_interest_rate = float(input("Enter savings account interest rate (in percentage): "))
    savings_months = int(input("Enter length of months for savings account: "))
    
    cd_balance = float(input("Enter CD account balance: "))
    cd_interest_rate = float(input("Enter CD account interest rate (in percentage): "))
    cd_months = int(input("Enter length of months for CD account: "))

    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    
    
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest_rate, savings_months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print("Interest earned on savings account:", interest_earned)
    print("Updated savings account balance:", updated_savings_balance)


    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest_rate, cd_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print("Interest earned on CD account:", interest_earned)
    print("Updated CD account balance:", updated_cd_balance)

if __name__ == "__main__":
    main()
