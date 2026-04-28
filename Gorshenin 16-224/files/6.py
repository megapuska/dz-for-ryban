f = open("numbers.txt", "r")
content = f.read()
f.close()

total = 0
count = 0
numbers = content.split()
for word in numbers:
    number = int(word)
    total = total + number
    count = count + 1

average = total / count
print(average)