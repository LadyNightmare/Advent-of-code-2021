import pandas

file = open("input.txt", "r").read()

data = pandas.DataFrame([x.split(';') for x in file.split('\n')])

data.drop(data.tail(1).index, inplace=True)

forward = 0
depth = 0

for line in range(0, len(data)):
    move_data = data[0][line].split(" ")
    direction = move_data[0]
    amount = int(move_data[1])
    if direction == 'forward':
        forward += amount
    elif direction == 'down':
        depth -= amount
    else:
        depth += amount


print(f"The result is {forward*depth}")