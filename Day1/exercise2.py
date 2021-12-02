import pandas

file = open("input2.txt", "r").read()

data = pandas.DataFrame([x.split(';') for x in file.split('\n')], columns=[0], dtype='int')

data.drop(data.tail(1).index, inplace=True)

increased_measure = 0

for i in range(0, len(data)-3):
    if data[0][i] + data[0][i+1] + data[0][i+2] < data[0][i+1] + data[0][i+2] + data[0][i+3]:
        print(f"{data[0][i]} is lower than {data[0][i + 1]}")
        increased_measure += 1

print(f"The result is {increased_measure}")