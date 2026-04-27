f = open("numbers.txt", "r")
for line in f:
    print(line.strip())
f.close()