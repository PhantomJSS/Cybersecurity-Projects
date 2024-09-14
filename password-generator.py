import random
import string

def password_generator (length: int  = 20):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for x in range(length))
    return password

choice = str(input("Would you like a new password?: "))

if(choice.lower() == "yes"):
    newpass = password_generator()
    print(f"Generated Password: {newpass}")
else:
    print("Maybe next time!")