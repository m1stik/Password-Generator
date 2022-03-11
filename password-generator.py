import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Data input
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_unmixed = []

#Generating sequence of chars
for step in range(1, nr_letters + 1):
    password_unmixed.append(random.choice(letters))
for step in range(1, nr_symbols + 1):
    password_unmixed.append(random.choice(symbols))
for step in range(1, nr_numbers + 1):
    password_unmixed.append(random.choice(numbers))

#Shuffling the sequence
random.shuffle(password_unmixed)

#Converting list to string
password_string = ''.join(password_unmixed)

#Password output
print(f"Here is your password: {password_string}")