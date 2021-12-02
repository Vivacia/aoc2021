def p1():
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

def p2():
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()

    start = -1
    curr = 0
    for i in range(len(Lines)-2):
        num1 = int(Lines[i])
        num2 = int(Lines[i+1])
        num3 = int(Lines[i+2])

        sum = num1 + num2 + num3

        if sum > curr:
            start += 1

        curr = sum

    print(start)

p2()