print("welcome to the tip calculator")
bill = float(input("What was the total bill? "))
tip_percent = int(input("What percent would you like to tip? 10, 12 or 15? "))
no_of_people = int(input("How many people to split the bill? "))

total_bill = bill+ (bill * tip_percent) / 100
print("each person should pay")
print(round(total_bill/no_of_people, 2))





