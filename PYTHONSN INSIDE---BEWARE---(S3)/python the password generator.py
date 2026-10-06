import secrets
import string
from random import randint as r

# Define the character set
alphabet = string.ascii_letters + string.digits + string.punctuation
# Set desired password length
password_length = r(1,30)
# Generate password
password = ''.join(secrets.choice(alphabet) for i in range(password_length))
print(f"Generated password: {password}")


while True:
    password = ''.join(secrets.choice(alphabet) for i in range(16))
    if (sum(c.islower() for c in password) >= 4 and
        sum(c.isupper() for c in password) >= 4 and
        sum(c.isdigit() for c in password) >= 4):
        break
print(f"Stronger password:{password}")

