import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "!@#$%^&*.()[]-,/ "

upper = True
lower = True
nums = True
syms = True

all_str = ""

if upper:
    all_str += uppercase_letters
if lower:
    all_str += lowercase_letters
if nums:
    all_str += digits
if syms:
    all_str += symbols

length = 15
amount = 10

for i in range(amount):
    password = "".join(random.sample(all_str, length))
    print(password)