print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_amount = (tip/100)*bill
total_bill = bill + tip_amount
per_person= round(total_bill/people, 2)
print(f"Your total amount to be paid by each person is = ${per_person}")



