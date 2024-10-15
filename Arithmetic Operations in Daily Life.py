#Task 1
#Grocery Store Math: Calculate the total cost of three items you'd commonly find in a grocery store, given their individual prices.
price_of_bread = 3.15
price_of_butter = 1.25
price_of_jelly = 2.50
total_cost = price_of_bread + price_of_butter + price_of_jelly
print("The total cost of groceries is", total_cost)

#Task 2
#Bank Interest: If you have a savings account with a particular initial amount and a fixed yearly interest rate, calculate the total amount in your account after a year.
#So if you had $10,000 at a 7% interest write code that would tell us the amount at the end of the yer.
initial_amount = input("What is your initial account value?")
initial_amount = float(initial_amount) #varible type needs to be converted to float
yearly_interest_rate = input("What is your yearly interest rate?")
yearly_interest_rate = float(yearly_interest_rate) #variable type needs to be conveted to float
interest_as_a_percent = yearly_interest_rate / 100 #interest is expressed as a decimal out of the whole number 1. So we are converting our input into that form so we can use it in a mathematical equation in the next step
total_after_a_year = initial_amount + initial_amount * interest_as_a_percent
print("After one year at your interest rate, your account will have", total_after_a_year, "dollars in it.")