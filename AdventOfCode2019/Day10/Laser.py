from pprint import *
import math

filename = "input.txt"
file = open(filename,"r")
data = file.read()[:-1]

data = data.split("\n")
pprint(data)

maximum = 0
pos = [0,0]

def CanSee(x,y):
    if data[y][x] == ".":
        return [],[]

    angles = []
    asteroids = []
        
    for _y in range(len(data)):
        for _x in range(len(data[_y])):
            if data[_y][_x] == ".":
                continue

            if x == _x and y == _y:
                continue

            rads = math.atan2(y-_y,x-_x)
            if rads in angles:
                index = angles.index(rads)
                pos = asteroids[index]
                dist1 = math.sqrt((pos[0] - x)**2 + (pos[1] - y)**2)
                dist2 = math.sqrt((_x - x)**2 + (_y - y)**2)  
                if(dist2 < dist1):
                    asteroids[index] = [_x,_y]
                continue
            angles.append(rads)
            asteroids.append([_x,_y])
            
    return angles, asteroids

for y in range(len(data)):
    for x in range(len(data[y])):
        angles, roids = CanSee(x,y)
        
        if len(angles) > maximum:
            maximum = len(angles)
            pos = [x,y]

print(maximum)
print(pos)
line = data[pos[1]]
line = line[:pos[0]] + "X" + line[pos[0]+1:]
data[pos[1]] = line
pprint(data)

def AsteroidCount():
    count = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "#":
                count = count + 1

    return count

def AngleFromYAxis(position):
    global pos
    angle = math.atan2(position[0]-pos[0],position[1]-pos[1])
    angle = 180 + math.degrees(angle)
    if angle < 0:
        angle = 360 + angle
    return angle

def UpdateData(position,value):
    global data    
    line = data[position[1]]
    line = line[:position[0]] + value + line[position[0]+1:]
    data[position[1]] = line
    
AngleFromYAxis([0,0])
vaporised = 0
while AsteroidCount() > 0:
    angles, asteroids = CanSee(pos[0],pos[1])
    asteroids.sort(key=AngleFromYAxis)
    length = len(asteroids)
    for i in range(length):
        vaporise = asteroids.pop()
        vaporised = vaporised + 1
        UpdateData(vaporise,".")   
        print("Vaporised: " + str(vaporised) + " at position: " + str(vaporise))
