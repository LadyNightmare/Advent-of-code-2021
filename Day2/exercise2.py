import pandas

file = open("input2.txt", "r").read()

data = pandas.DataFrame([x.split(';') for x in file.split('\n')], columns=[0], dtype='int')

data.drop(data.tail(1).index, inplace=True)

forward = 0
depth = 0
aim = 0

for line in range(0, len(data)):
    move_data = data[0][line].split(" ")
    direction = move_data[0]
    amount = int(move_data[1])
    if direction == 'forward':
        forward += amount
        depth += aim*amount
    elif direction == 'down':
        aim += amount
    else:
        aim -= amount


print(f"The result is {forward*depth}")