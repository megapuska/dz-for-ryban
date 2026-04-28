f = open("numbers.txt", "r")
content = f.read()
f.close()

total = 0
numbers = content.split()
for word in numbers:
    number = int(word)
    total = total + number

print(total)