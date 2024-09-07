import string
import random


## characters to generate password from
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
	## length of password from the user
	length = int(input("\nEnter password length: "))
	print("")
	## shuffling the characters
	random.shuffle(characters)
	
	## picking random characters from the list
	password = []
	for i in range(length):
		password.append(random.choice(characters)) #genera la contraseña.

	## shuffling the resultant password
	random.shuffle(password)

	## converting the list to string
	## printing the list
	print("Password: ")
	print("".join(password))



## invoking the function
generate_random_password()

print("")