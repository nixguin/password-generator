import random
import string
print("Welcome to the PyPassword Generator!")
nr_letters=int(input("How many letters would you like in your password?\n"))
nr_symbols=int(input(f"How many symbol would you like?\n"))
nr_numbers=int(input(f"How many numbers would you like?\n"))

password_letters = ''.join(random.choice(string.ascii_letters) for _ in range(nr_letters))
password_numbers = ''.join(random.choice(string.digits) for _ in range(nr_numbers))
password_symbol = ''.join(random.choice(string.punctuation) for _ in range(nr_symbols))

password_list=list(password_letters+password_numbers+password_symbol)
random.shuffle(password_list)
password=''.join(password_list)

print(f"Here is your strong password",password)