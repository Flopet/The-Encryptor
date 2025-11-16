import os
from os.path import exists
import time
from cryptography.fernet import Fernet as Fn

# prereqs
def p(text):
	print(text)
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
skip_files = ["the_encryptor_v2.py", ".keyfile"]

#def reset_files():
#		files = []
files = []
def load_files(skip):
	global files
	files = []
	for file in os.listdir():
		if os.path.isfile(file):
			files.append(file)
		for l in skip:
			if file == l:
				files.remove(l)





# encryptor
def ec(target_files, encryption_key):
	for file in target_files:
		with open(file, "rb") as theFile:
			original_contents = theFile.read()
		encrypted_contents = Fn(encryption_key).encrypt(original_contents)
		with open(file, "wb") as theFile:
			theFile.write(encrypted_contents)
	p("Encryption complete!")

# decryptor
def dc(target_files):
	with open(".keyfile", 'rb') as keyfile:
		dc_key = keyfile.read()
	for file in target_files:
		with open(file, "rb") as theFile:
			encrypted_contents = theFile.read()
		decrypted_contents = Fn(dc_key).decrypt(encrypted_contents)
		with open(file, "wb") as theFile:
			theFile.write(decrypted_contents)
	p("Files decrypted!")


#  Remove file command
def remove_file(removed_file):
	skip_files.append(removed_file)







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
				new_key = Fn.generate_key()
				with open(".keyfile", 'wb') as key_file:
					key_file.write(new_key)
				p("Key has been generated.")
				with open(".keyfile", 'rb') as keyfile:
					new_key = keyfile.read()
				return new_key
			else:
				p("Original key will be used.")
				with open('.keyfile', 'rb') as keyfile:
					existing_key = keyfile.read()
				return existing_key
		else:
			p("Original key will be used.")
			with open('.keyfile', 'rb') as keyfile:
				existing_key = keyfile.read()
			return existing_key
	else:

		p("Generating new key to .keyfile")
		new_key = Fn.generate_key()
		with open(".keyfile", "wb") as key_file:
			key_file.write(new_key)
		return new_key






# commands

def new_command(current_key):
	cmd = input("> ")
	cmd = cmd.lower()
	if cmd == "help":
		p('''
	encrypt 			Encrypts all files in the CWD
	decrypt 			Decrypts all files within the CWD.
	makey 				Make a new file containing the decryption key if needed.
	quit, q				Close Program
		''')
		new_command(current_key)
	elif cmd == "encrypt":
		ec(files, current_key)
		time.sleep(2)
		new_command(current_key)
	elif cmd == "decrypt":
		dc(files)
		time.sleep(2)
		new_command(current_key)
	elif cmd == "makey":
		key_declaration()
		p("Key file generated!")
		time.sleep(2)
		new_command(current_key)
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
		new_command(current_key)





# BEGIN
def begin():
	clear()
	load_files(skip_files)
	p("""
	-------------------------------------------------------------------------------------------------------
	Welcome to the file encryptor. All files within the current directory will be targeted by this program.

	Type "help" for a list of commands.
	-------------------------------------------------------------------------------------------------------
	Files selected: """ + str(files) + """
	\n
	\n
	""")
	current_key = key_declaration()
	new_command(current_key)
begin()
