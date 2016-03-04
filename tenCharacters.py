#Author: Ami
#Date: March 4

#opens/reads file
f = open("input.txt", "r")
lines = f.readlines()
f.close()

#creates/wipes output file
f = open("output.txt", "w")

#scans every line(word) and tests if its over 10 characters long
for word in lines:
	if len(word) < 11:
		f.write(word)
		
	if len(word) > 10:
		number = len(word) 
		left = number - 10
		word = word[: - left]  #cuts off at 10 letters
		f.write(word + "\n")
	