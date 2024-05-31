text = "It was a bright cold day in april, and the clocks were striking thirteen."

res = {}

for char in text: 
    if char.isalpha():
        char = char.lower()
        if char not in res:
            res.setdefault(char, 1)
        else: res[char] += 1
    


print(res)