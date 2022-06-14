
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letters_choice = ''
for i in range(1, nr_letters + 1):
    l = random.choice(letters)
    letters_choice += l

numbers_choice = ''
for i in range(1, nr_numbers + 1):
    n = random.choice(numbers)
    numbers_choice += n

symbols_choice = ''
for i in range(1, nr_symbols + 1):
    s = random.choice(symbols)
    symbols_choice += s

password_provisor = numbers_choice + symbols_choice + letters_choice

from random import sample
password_result_list = sample(password_provisor, len(password_provisor))

password_result = ''
for i in password_result_list:
    password_result += i

print(password_result)






