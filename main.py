#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!\n")
bill = input("What was the total bill? \n$")
tip = input("How much tip would you like to give? 10, 12, or 15?\n")
people = input("How many people to split the bill?\n")
bill_float = float(bill)
tip_int = int(tip)
people_int = int(people)
tip_percent = tip_int / 100
tip_amount = (bill_float / 5) * (1 + tip_percent)
tip_amount_round = round(tip_amount, 2)
print(f"Each person should pay: ${tip_amount_round}")