"""
In Part A, we are going to determine how long it will take you to save enough
money to make the down payment.

Test Case 1
>>>
Enter your annual salary: 120000
Enter the percent of your salary to save, as a decimal: .10
Enter the cost of your dream home: 1000000
Number of months: 183
>>>
Test Case 2
>>>
Enter your annual salary: 80000
Enter the percent of your salary to save, as a decimal: .15
Enter the cost of your dream home: 500000
Number of months: 105
>>>
"""

# Collect input data from user.
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

def monthsToDownPayment(total_cost, annual_salary, portion_saved):
    # Create variables.
    # Percentage of monthly salary dedicated to down payment.
    portion_down_payment = 0.25
    down_payment = portion_down_payment*total_cost

    # Annual return on savings.
    r = 0.04

    # Takes annual salary input from user and converts to monthly salary.
    monthly_salary = annual_salary/12

    # Initializes number of months necessary to cover down payment.
    number_of_months = 0
    
    # Initialize current savings counter.
    current_savings = 0
    
    # Loop to find number of saving months required for down payment.
    while current_savings < down_payment:
        current_savings += current_savings*(r/12)
        amount_saved = monthly_salary * portion_saved
        current_savings += amount_saved
        number_of_months += 1
        
    # Print answer.
    print(f"Number of months: {number_of_months}")
    
monthsToDownPayment(total_cost, annual_salary, portion_saved)