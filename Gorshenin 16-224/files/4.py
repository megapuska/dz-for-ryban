f = open("names.txt", "r")
lines = f.readlines()
f.close()

count = 0
for line in lines:
    count = count + 1

print(count)