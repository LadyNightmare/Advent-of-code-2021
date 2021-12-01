import pandas

file = open("input.txt", "r").read()

data = pandas.DataFrame([x.split(';') for x in file.split('\n')])

increased_measure = 0

for i in range(0, len(data)-1):
    if data[0][i] < data[0][i+1]:
        print(f"{data[0][i]} is lower than {data[0][i + 1]}")
        increased_measure += 1

print(f"The result is {increased_measure}")