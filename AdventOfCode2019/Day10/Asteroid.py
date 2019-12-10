from pprint import *
import math

filename = "input.txt"
file = open(filename,"r")
data = file.read()[:-1]

data = data.split("\n")
pprint(data)

maximum = 0
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == ".":
            continue

        angles = []
        
        for _y in range(len(data)):
            for _x in range(len(data[_y])):
                if data[_y][_x] == ".":
                    continue

                if x == _x and y == _y:
                    continue

                rads = math.atan2(y-_y,x-_x)
                if rads in angles:
                    continue
                angles.append(rads)
        if len(angles) > maximum:
            maximum = len(angles)

print(maximum)
                    
