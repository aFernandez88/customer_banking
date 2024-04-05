"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account
# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
class Account:
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest
savings_account = Account(1000, 0)
        
    
    
     # Calculate interest earned
     # ADD YOUR CODE HERE
def simple_interest(principal, interest_rate, time):
    interest_earned = principal * (interest_rate / 100) * time
    return interest_earned

    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
def updated_blance(balance, interest_rate, time):
    interest_earned = simple_interest(balance, interest_rate, time)
    new_balance = balance + interest_earned
    return new_balance
    
    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    savings_acc.set_balance(updated_balance)

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    savings_acc.set_interest(interest_earned)

    # Return the updated balance and interest earned.
    # ADD YOUR CODE HERE
    def updated_balance(balance, interest_rate, time):
     interest_earned = simple_interest(balance, interest_rate, time)
     new_balance = balance + interest_earned
    return new_balance, interest_earned

