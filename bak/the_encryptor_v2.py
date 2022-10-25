import os
from os.path import exists
import time
from cryptography.fernet import Fernet as fn

# prereqs
def p(input):
	print(input)
def clear():
	os.system("clear")

def goodbye():
	clear()
	i = 0
	bye = 'Goodbye.'
	while i < 25:
		clear()
		p(bye)
		time.sleep(0.03)
		i += 1
		bye += "."

key = ""
files = []
skip_files = ["the_encryptor_v2.py", ".keyfile"]
for file in os.listdir():
	if file == skip_files[file]:
		continue
	if os.path.isfile(file):
		files.append(file)







# encryptor
def ec(files, key):
	for file in files:
		with open(file, "rb") as thefile:
			original_contents = thefile.read()
		encrypted_contents = fn(key).encrypt(original_contents)
		with open(file, "wb") as thefile:
			thefile.write(encrypted_contents)
	p("Encryption complete!")

# decryptor
def dc(files):
	with open(".keyfile", 'rb') as key:
		dc_key = key.read()
	for file in files:
		with open(file, "rb") as thefile:
			encrypted_contents = thefile.read()
		decrypted_contents = fn(dc_key).decrypt(encrypted_contents)
		with open(file, "wb") as thefile:
			thefile.write(decrypted_contents)
	p("Files decrypted!")








#does the user have a copy of the key? >> Use this part of the program with the implementation of passwords.
def key_declaration():

	if exists(".keyfile"):
		p("A key already exists.")
		x = input("Do you want to generate a new key (y/n)? ")
		x = x.lower()
		if x == "y":
			confirmation = input("Are you sure? This will overwrite the existing key (y/n)! " )
			confirmation = confirmation.lower()
			if confirmation == 'y':
				key = fn.generate_key()
				with open(".keyfile", 'wb') as key_file:
					key_file.write(key)
				p("Key has been generated.")
				key = open(".keyfile", 'rb')
				key = key.read()
				return key
				time.sleep(2)
			else:
				p("Original key will be used.")
				key = open('.keyfile', 'rb')
				key = key.read()
				return key
				time.sleep(2)
		else:
			p("Original key will be used.")
			key = open('.keyfile', 'rb')
			key = key.read()
			return key
			time.sleep(2)
	else:

		p("Generating new key to .keyfile")
		key = fn.generate_key()
		with open(".keyfile", "wb") as key_file:
			key_file.write(key)
		return key
		time.sleep(2)






def remove_file(removed_file):
	files = files.append(removed_file)








# commands

def new_command(key):
	cmd = input("> ")
	cmd = cmd.lower()
	if cmd == "help":
		p('''
	encrypt 			Encrypts all files in the CWD
	decrypt 			Decrypts all files within the CWD.
	makey 				Make a new file containing the decryption key if needed.
		''')
		new_command(key)
	elif cmd == "encrypt":
		ec(files, key)
		time.sleep(2)
		new_command(key)
	elif cmd == "decrypt":
		dc(files)
		time.sleep(2)
		new_command(key)
	elif cmd == "makey":
		key_declaration()
		p("Key file generated!")
		time.sleep(2)
		new_command(key)
	elif cmd == 'remfile':
		removed_file = input("What file would you like to remove? ")
		remove_file(removed_file)
		p("File Removed!")
		p("Restarting...")
		time.sleep(2)
		begin()
	elif cmd == 'quit' or cmd == 'q':
		goodbye()
		clear()
		quit()
	else:
		p("That is not a recognized command, please try again...")
		new_command(key)





# BEGIN
def begin():
	clear()
	p("""
	-------------------------------------------------------------------------------------------------------
	Welcome to the file encryptor. All files within the current directory will be targeted by this program.

	Type "help" for a list of commands.
	-------------------------------------------------------------------------------------------------------
	Files selected: """ + str(files) + """
	\n
	\n
	""")
	key = key_declaration()
	new_command(key)
begin()
