import os

password = []
i = 0

word_file = open("wordlist.txt", mode="r")
word_list = word_file.read().split("\n")

while i < 4:

	int.from_bytes(os.urandom(2), byteorder = "big") % len(word_list)
	password.append(word_list[])
	i += 1

print("Your new password is: %s" % ' '.join(password))
