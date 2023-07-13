# #Heads or Tails:
# #Remember to use the random module
# #Hint: Remember to import the random module here at the top of the file. 🎲
	 
# #Write the rest of your code below this line 👇
# import random

# number = random .randint(0,1)
# if number == 0:
#     print("Tails")
# else:
#     print("Heads")



# #Banker's Roulette:
# # Import the random module here

# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# import random

# paying_person_index = random.randint(0,len(names)-1)
# paying_person = names[paying_person_index]
# print(f"{paying_person} is going to buy the meal today!")


# #Banker's Roulette Improvised:
# # Import the random module here

# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# import random

# paying_person = random.choice(names)
# print(f"{paying_person} is going to buy the meal today!")


# #Treasure Map exercise
# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# column = int(position[0]) - 1
# row = int(position[1]) - 1

# map[row][column] = "X"
# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")

#another way to solve this exercise is to assign the row to a list and then modify the column value. This solves the problem using
#single indices itself, rather than double indices

# Final Project Rock-Paper-Scissor
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

moves = [rock,paper,scissors]

user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors\n"))
user_move = moves[user_choice]
print(f"{user_move}\n")

computer_choice = random.randint(0,2)
computer_move = moves[computer_choice]

print(f"Computer Chose:\n\n{computer_move}\n")

if user_choice == computer_choice:
  print("It's a draw")
elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
  print("You Win!")
else:
  print("You Lose!")