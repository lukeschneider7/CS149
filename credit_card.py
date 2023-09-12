"""Lab 6 Credit Card.

Work with conditionals and simulate a credit card statement.

Author: Luke Schneider
Version: 09/12/2023
Attribution: I got help working through the lab from Professor Chao in class
"""

if __name__ == '__main__':
    # Input section
    prior_balance = float(input("Type the previous balance "))
    # If the user input is not between -5000 and 5000
    # set prior balance to zero.
    # ** FINISH THE LOGIC HERE
    if prior_balance < -5000 or prior_balance > 5000:
        prior_balance = 0
    addtl_charges = float(input("Type the additional charges "))
    # Check that addtl_charges is >= 0 otherwise set it to zero.
    # ** FINISH THE CODE HERE
    if addtl_charges < 0:
        addtl_charges = 0
    # CALCULATIONS: perform the calculation of interest,
    # new balance, minimum payment
    # ** FINISH THE CODE HERE
    interest = (prior_balance * .02)
    if interest > 0:
        interest += addtl_charges * .02
    """ Take previous balance and additional charges and compute interest.
    If the prior_balance is zero or less, the interest is 0.
    If there was a prior_balance, the interest is 2% of the prior_balance plus the
    additional charges.
    """
    new_balance = prior_balance + addtl_charges + interest
    # ** FINISH THE CODE HERE
    
    """Take in the previous balance and additional charges and compute the minimum payment.

    $0.00 - for new balance less than $0
    new balance - for new balance between $0 and $49.99 (inclusive)
    $50.00 - for new balance between $50 and $300 (inclusive)
    20% of the new balance - for new balance over $300
    """
    min_payment = 0.0
    if new_balance > 0 and new_balance < 50:
        min_payment = new_balance
    elif new_balance >= 50 and new_balance <= 300:
        min_payment = 50.00
    elif new_balance > 300:
        min_payment = .2 * new_balance

    # output the resulting credit card statement
    print("")
    print("CS CARD International Statement")
    print("===============================")
    print(f"Previous balance:    $ {prior_balance:8.2f}\n")
    print(f"Additional charges:  $ {addtl_charges:8.2f}\n")
    print(f"Interest:            $ {interest:8.2f}\n")
    print(f"New balance:         $ {new_balance:8.2f}\n")
    print(f"Minimum payment:     $ {min_payment:8.2f}\n")