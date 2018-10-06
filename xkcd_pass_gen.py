import os

password = []

word_file = open("wordlist.txt", mode="r")
word_list = word_file.read().split("\n")

while True:
	try: 
		password_len_option = int(input("Password Length: "))
		break
	except ValueError:
		print("Please only input positive integers.")

i = 0
while i < password_len_option:
	
	choice = int.from_bytes(os.urandom(2), byteorder = "little") % len(word_list)
	password.append(word_list[choice])
	i += 1

print("Your new password is: %s" % ' '.join(password))

