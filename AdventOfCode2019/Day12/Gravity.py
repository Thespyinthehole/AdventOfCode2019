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

steps = 1000
for i in range(steps):
    print("After " + str(i) + " steps:")
    for moon in data:
        print("pos=" + str(moon[0]) + ", vel=" + str(moon[1]))
    print()
    for moon in data:
        vel = moon[1]
        pos = moon[0]
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
        
    for moon in data:
        pos = moon[0]
        vel = moon[1]
        pos[0] = pos[0] + vel[0]
        pos[1] = pos[1] + vel[1]
        pos[2] = pos[2] + vel[2]

        moon[0] = pos
        

print("After " + str(steps) + " steps:")
for moon in data:
    print("pos=" + str(moon[0]) + ", vel=" + str(moon[1]))
print()

energies = []
for moon in data:
    pos = moon[0]
    vel = moon[1]
    pot = abs(pos[0]) + abs(pos[1]) + abs(pos[2])
    kin = abs(vel[0]) + abs(vel[1]) + abs(vel[2])
    total = pot * kin
    potStr = "pot: " + str(pos[0]) + " + " + str(pos[1]) + " + " + str(pos[2]) + " = " + str(pot) + "; "
    kinStr = "kin: " + str(vel[0]) + " + " + str(vel[1]) + " + " + str(vel[2]) + " = " + str(kin) + "; "
    totalStr = "total: " + str(pot) + " * " + str(kin) + " = " + str(total)
    print(potStr + kinStr + totalStr)
    energies.append(total)

totalSum = sum(energies)

print("Total energy: " + str(totalSum))
