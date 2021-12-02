def p1():
    file1 = open('input2.txt', 'r')
    Lines = file1.readlines()

    x = 0
    y = 0
    for line in Lines:
        line = line.split(" ")
        cmd = line[0]
        num = int(line[1])
        
        if cmd == "forward":
            x += num
        elif cmd == "down":
            y += num
        elif cmd == "up":
            y -= num

    print(x * y)


def p2():
    file1 = open('input2.txt', 'r')
    Lines = file1.readlines()

    x = 0
    y = 0
    aim = 0
    for line in Lines:
        line = line.split(" ")
        cmd = line[0]
        num = int(line[1])
        
        if cmd == "forward":
            x += num
            y += aim*num
        elif cmd == "down":
            # y += num
            aim += num
        elif cmd == "up":
            # y -= num
            aim -= num

    print(x * y)

p2()