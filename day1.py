file1 = open('input.txt', 'r')
Lines = file1.readlines()

start = -1
curr = 0
for line in Lines:
    num = int(line.strip())
    if num > curr:
        start += 1
    curr = num

print(start)