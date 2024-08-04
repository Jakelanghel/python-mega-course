# Coding Exercise 5

# Please code this exercise in your computer IDE.
#  For this exercise, download the members.txt file attached to the resources.
#  Then, create a program that:

# 1. prompts the user to enter a new member.

# 2. adds that member to members.txt at the end of the existing members. For example,
#  the user here has entered the member Solomon Right.
file = open("members.txt", "r")

# arr = file.read().split("\n")
print("Enter name")
name = input()
updated = f"{file.read()}{name}\n"
file = open("members.txt", "w")
file.write(updated)