import os

password = []
i = 0

word_file = open("wordlist.txt", mode="r")
word_list = word_file.read().split("\n")

print(len(word_list))


while i < 4:
	password.append(word_list[int.from_bytes(os.urandom(2), byteorder = "big") % len(word_list)])
	i += 1

print(password)
