import secrets as sc
import string

upper_letters = string.ascii_uppercase
lower_letters = string.ascii_lowercase
numbers = string.digits
symbols = string.punctuation

all_in_one = upper_letters + lower_letters + numbers + symbols

random_password = ''.join(sc.choice(all_in_one) for i in range(16))
print(random_password)
