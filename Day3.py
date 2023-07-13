##task 1
#number = int(input("Enter the number: "))

# if number % 2 == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")

# #task 2
# print("Welcome to the Roller Coaster!")
# height = int(input("Enter your height: "))

# if height >=120:
#     print("You are eligible for riding")
#     age = int(input("Enter your Age: "))
#     if age < 12:
#         print("Please pay $5.")
#     elif age <=18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")

# else:
#     print("Please grow up")

# #Exercise 3
# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# if size == "S":
#     bill = 15
# elif size == "M":
#     bill = 20
# elif size == "L":
#     bill = 25
# if add_pepperoni == "Y":
#     bill += 2
#     if size == "M" or size == "L":
#         bill += 1
# if extra_cheese == "Y":
#     bill += 1
# print(f"Your final bill is: ${bill}")


#Exercise 4
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
love_score1 = 0
love_score2 = 0
string1 = "true"
string2 = "love"

name = name1.lower() + name2.lower()

for i in string1:
    love_score1 += name.count(i)
for i in string2:
    love_score2 += name.count(i)

final_love = love_score1*10 + love_score2

if final_love < 10 or final_love > 90:
    print(f"Your score is {final_love}, you go together like coke and mentos.")
elif final_love > 40 and final_love < 50:
    print(f"Your score is {final_love}, you are alright together.")
else:
    print(f"Your score is {final_love}.")


