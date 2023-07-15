# #Interactive Exercise 1 - Finding avg height
# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆


# #Write your code below this row 👇
# sum = 0
# len = 0

# for height in student_heights:
#     sum += height
#     len += 1

# avg = round(sum/len)
# print(avg)



# #Interactive Exercise 2 - Finding max height
# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# highest_score = 0

# for score in student_scores:
#     if highest_score < score:
#         highest_score = score

# print(f"The highest score in the class is: {highest_score}")




#Interactive Exercise 3 - Sum of even nos. upto 100
# #Write your code below this row 👇
# sum = 0
# for number in range(2,101,2):
#     sum += number

# print(sum)



## ICE 4 - Fizzbuzz
# #Write your code below this row 👇
# for number in range(1,101):
#     if number%3==0 and number%5==0:
#         print("FizzBuzz")
#     elif(number%3==0):
#         print("Fizz")
#     elif(number%5==0):
#         print("Buzz")
#     else:
#         print(number)



# #Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# letter_list = []

# for num in range(0, nr_letters):
#     letter_list.append(random.choice(letters))

# for num in range(0, nr_symbols):
#     letter_list.append(random.choice(symbols))

# for num in range(0, nr_numbers):
#     letter_list.append(random.choice(numbers))

# random.shuffle(letter_list)

# final_pass = ''.join(letter_list)

# print(final_pass)


#Password Generator Project v2
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

final_pass_list = random.sample(letters, nr_letters) + random.sample(numbers, nr_numbers) + random.sample(symbols, nr_symbols)
random.shuffle(final_pass_list)
final_pass = ''.join(final_pass_list)

print(final_pass)