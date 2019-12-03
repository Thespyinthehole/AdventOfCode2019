
movementString = """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83"""
wires = movementString.split("\n")
wires[0] = wires[0].split(",")
wires[1] = wires[1].split(",")

beenBefore = [[0,0]]
junctions = []
for wire in wires:
    position = [0,0]
    for movement in wire:
        direction = movement[0]
        value = int(movement[1:])
        for i in range(value):
            move = [0,0]
        
            if (direction == "U"):
                move[1] = 1
            elif (direction == "D"):
                move[1] = -1
            elif (direction == "R"):
                move[0] = 1
            elif (direction == "L"):
                move[0] = -1
            
            position[0] = position[0] + move[0]
            position[1] = position[1] + move[1]
        
            if(position in beenBefore):
                if(not position in junctions):
                    junctions.append(position)
            else:
                beenBefore.append(position)
        

print(junctions)
