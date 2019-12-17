import numpy as np

filename = "input.txt"
file = open(filename,"r")
data = file.read()

b = "<>=xyz"
for char in b:
    data = data.replace(char,"")

data = data.split("\n")[:-1]
for i in range(len(data)):
    pos = data[i].split(",")
    for o in range(len(pos)):
        pos[o] = int(pos[o])
    data[i] = [pos,[0,0,0]]

steps = 50000
start = [[],[],[],[]]
startVel = [[],[],[],[]]
values = [[],[],[],[],[],[]]
for i in range(steps):
    for moon in data:            
        vel = moon[1]
        pos = moon[0]
        if i == 0:
            start[data.index(moon)] = pos.copy()
            startVel[data.index(moon)] = vel.copy()
        for other in data:
            if other == moon:
                continue
            _pos = other[0]

            if pos[0] < _pos[0]:
                vel[0] = vel[0] + 1
            elif pos[0] > _pos[0]:
                vel[0] = vel[0] - 1
    
            if pos[1] < _pos[1]:
                vel[1] = vel[1] + 1
            elif pos[1] > _pos[1]:
                vel[1] = vel[1] - 1
                
            if pos[2] < _pos[2]:
                vel[2] = vel[2] + 1
            elif pos[2] > _pos[2]:
                vel[2] = vel[2] - 1
        moon[1] = vel

    totals = [0,0,0,0,0,0]
    for o in range(len(data)):
        moon = data[o]
        pos = moon[0]
        vel = moon[1]
        pos[0] = pos[0] + vel[0]
        pos[1] = pos[1] + vel[1]
        pos[2] = pos[2] + vel[2]

        if pos[0] == start[o][0]:
            totals[0] = totals[0] + 1

        if pos[1] == start[o][1]:
            totals[1] = totals[1] + 1

        if pos[2] == start[o][2]:
            totals[2] = totals[2] + 1

        if vel[0] == startVel[o][0]:
            totals[3] = totals[3] + 1

        if vel[1] == startVel[o][1]:
            totals[4] = totals[4] + 1

        if vel[2] == startVel[o][2]:
            totals[5] = totals[5] + 1
             
    if totals[0] == 4 and len(values[0]) == 0:
        values[0].append(i+2)
    if totals[1] == 4 and len(values[1]) == 0:
        values[1].append(i+2)
    if totals[2] == 4 and len(values[2]) == 0:
        values[2].append(i+2)

    
    if totals[3] == 4 and len(values[3]) == 0:
        values[3].append(i+1)
    if totals[4] == 4 and len(values[4]) == 0:
        values[4].append(i+1)
    if totals[5] == 4 and len(values[5]) == 0:
        values[5].append(i+1)

for i in range(len(values)):
    values[i] = values[i][0]
print(values)
print(np.lcm.reduce(values))
