# print("Hello"[0])
#
# print(123_456_700 + 35)

# num_char = len(input("What is your name\n"))
# # print(type(num_char))
# str_num_char = str(num_char)
# print("your name has " + str_num_char + " characters")

# two_digit_number = input("Enter a two digit number")
#
# str_two_digit_number = str(two_digit_number)
#
# first_digit = str_two_digit_number[0]
# second_digit = str_two_digit_number[1]
#
# sum_of_digits = int(first_digit) + int(second_digit)
# print(sum_of_digits)

# f-Strings

# score = 0
# height = 1.8
# isWining = True
#
# print(f"your score is {score} and you height is {height}. You are winning {isWining}")

# how many days, weeks and months you have until you reach 90

years_left = 90 - int(input("enter you age"))

month_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365
print(f"you have {days_left} days,{weeks_left} weeks and {month_left} months")