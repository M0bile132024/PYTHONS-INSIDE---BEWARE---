#Python the password cracker v1.0
#By: M0bile132022
#Date: 2025-06-21
#Description: This script attempts to guess a password by generating all possible combinations of characters.
# It uses itertools to create combinations of characters and checks each guess against the provided password.
# This script is for educational purposes only. Use responsibly and ethically.
import string
import itertools, time

def guess_password(password,chars):
    found=False
    start = time.time()
    
    
    
    attempts = 0
    for password_length in range(1, 9):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == password:
              found = True
              end = time.time()
              duration = end - start
              return f'password is {guess} found in {attempts} attempts in {duration:.2f} seconds'
            #print(guess)
    if found is False:
      return "Password not found" 


#ascii letters and digitals
alpha = chars = string.ascii_letters + string.digits
#extended characters

#ascii letters, digits, special characters and whitespace
extended = chars = string.ascii_letters + string.digits + string.punctuation + string.whitespace 

#password to check
password = input("Enter the password to guess: ")
extended_or_not = input("Do you want to use extended characters? (yes/no): ").strip().lower()
if extended_or_not == 'yes':
    charact = extended
    print("e")
else:
    charact = alpha
    print("a")



#call function and print return value
print(guess_password(password,charact))
