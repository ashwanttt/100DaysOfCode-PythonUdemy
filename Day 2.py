# print(type(int("9")))

#Operator Exercise
# 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
# print(int(float(weight)/float(height)**2))

# score = 0
# print("score is :" + score)

# weeks and days left exercise
# # 🚨 Don't change the code below 👇
# age = input("What is your current age? ")
# #🚨 Don't change the code above 👆

# #Write your code below this line 👇
# months_left = int(90*12 - int(age)*12)
# weeks_left = int(90*52 - int(age)*52)
# days_left = int(90*365 - int(age)*365)
# print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left")
# #another way to do this is to find years left and then multiply by 365 or 12 or 52

#Tip calculator final project
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = float(input("What is the total bill?\n$"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
number = int(input("How many people to split the bill?\n"))
split_up = (bill * (1 + tip/100)/number)
final = "{:.2f}".format(split_up)
print(f"Each person should pay: ${final}")
print(type(final))
