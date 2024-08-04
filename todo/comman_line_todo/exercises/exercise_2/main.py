# Coding Exercise 5

# Please code this exercise in your computer IDE.
#  For this exercise, download the members.txt file attached to the resources.
#  Then, create a program that:

# 1. prompts the user to enter a new member.

# 2. adds that member to members.txt at the end of the existing members. For example,
#  the user here has entered the member Solomon Right.


# John Smith
# Sen Lakmi
# Sono Octonot

new_member = input("Enter name:")
file = open("members.txt", "r")
existing_members = file.readlines()
file.close()
existing_members.append(new_member + "\n")
file = open("members.txt", "w")
existing_members = file.writelines(existing_members)
file.close()

