#Author: Ami
#Date: March 4


f = open("input.txt", "r+")
text = f.read()
f.close()

#print(text)

f = open("output.txt", "w")
f.write(text + "\n")
