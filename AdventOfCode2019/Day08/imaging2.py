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

image = "2" * 25 * 6
reverse = data.copy()
reverse.reverse()
for datam in reverse:
    for i in range(len(datam)):
        char = datam[i]
        if char == "2":
            continue
        
        image = image[:i] + char + image[i+1:]

image = [image[i:i+n] for i in range(0, len(image), n)]
image = [image[i:i+m] for i in range(0, len(image), m)]
image = image[0]
for x in range(len(image)):
    image[x] = image[x].replace("0"," ")
pprint(image)
