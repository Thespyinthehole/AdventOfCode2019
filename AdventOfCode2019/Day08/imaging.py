from pprint import *
import sys
filename = "input.txt"
file = open(filename,"r")
data = file.read()[:-1]
n = 25
data = [data[i:i+n] for i in range(0, len(data), n)]
m = 6
data = [data[i:i+m] for i in range(0, len(data), m)]

data = ["".join(data[i]) for i in range(len(data))]

minCount = sys.maxsize
layer = []
for datam in data:
    count = datam.count("0")
    if (count < minCount):
        layer = datam
        minCount = count

ones = layer.count("1")
twos = layer.count("2")

print(ones * twos)
