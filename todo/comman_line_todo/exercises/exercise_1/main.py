# Write a program that reads the essay.txt file 
# and returns the number of characters contained in the file.

   

def count():
    res = 0
    file = open("essay.txt", "r")
    arr = list(file.read())
    print(len(arr))


file = open("file.txt", "w")
file.write("snail")
