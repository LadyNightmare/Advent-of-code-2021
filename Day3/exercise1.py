import pandas

file = open("input.txt", "r").read()

data = pandas.DataFrame([x.split(';') for x in file.split('\n')])

data.drop(data.tail(1).index, inplace=True)

zero = 0
one = 0
gamma = ''
epsilon = ''


for i in range(0, len(data[0][0])):
    for j in range(0, len(data)):
        if data[0][j][i] == '0':
            zero += 1
        else:
            one += 1
    if zero > one:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
    zero = 0
    one = 0

print(f"The binary result is: gamma {gamma} epsilon {epsilon}")


def binary_to_decimal(binary):
    binary = int(binary)
    decimal, i, n = 0, 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


print(f"The decimal result is: gamma {binary_to_decimal(gamma)} epsilon {binary_to_decimal(epsilon)}")

result = binary_to_decimal(gamma) * binary_to_decimal(epsilon)

print(f"The final result is {result}")
