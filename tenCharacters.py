#Author: Ami
#Date: March 4


f = open("input.txt", "r")
lines = f.readlines()
f.close()

f = open("output.txt", "w")

for word in lines:
	if len(word) < 11:
		
		f.write(word)
		
	if len(word) > 10:
		number = len(word)
		left = number - 10
		word = word[: - left]
		f.write(word + "\n")
	