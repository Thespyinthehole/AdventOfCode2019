from graphics import *       
import sys

width = 42
height = 42
pos = [int(width/2),int(height/2)]
maze = [[[-1,1,[]].copy() for i in range(width)].copy() for o in range(height)]
moves = []
lastDirection = 0
maze[pos[1]][pos[0]][0] = 1
win = GraphWin("Maze",615,615, autoflush=False)

def clear():
    for item in win.items[:]:
        item.undraw()
    win.update()

def DrawMaze():
    size = 15
    for y in range(len(maze)):
        row = maze[y]
        for x in range(len(row)):
            datam = row[x]
            pt = Point(x*size,y*size)
            color = "white"
            if datam == 0:
                color = "black"
            if datam == 2:
                color = "green"
            if datam == 3:
                color = "blue"
            if pos == [x,y]:
                color = "red"
            
            rec = Rectangle(pt,Point((x+1)*size,(y+1)*size))
            rec.setFill(color)
            rec.draw(win)
    win.update()
    
def GetValue(pc,stack,parameters,i):
    global relativePos
    if(i-1 < len(parameters)):
        if(parameters[i-1] == '1'):
            return int(stack[pc+i])
        if(parameters[i-1] == '2'):
            offset = int(stack[pc+i])
            return int(stack[relativePos+offset])
    return int(stack[int(stack[pc+i])])

def SetValue(pc,stack,parameters,i,value):
    if(i-1 < len(parameters)):
        if(parameters[i-1] == '2'):
            offset = int(stack[pc+i])
            stack[relativePos+offset] = str(value)
            return
    stack[int(stack[pc+i])] = str(value)
    
def Addition(pc,stack,params):
    part1 = GetValue(pc,stack,params,1)
    part2 = GetValue(pc,stack,params,2)
    value = part1 + part2
    SetValue(pc,stack,params,3,value)
    pc = pc + 4
    return pc, stack

def Multiply(pc,stack,params):
    part1 = GetValue(pc,stack,params,1)
    part2 = GetValue(pc,stack,params,2)
    value = part1 * part2
    SetValue(pc,stack,params,3,value)
    pc = pc + 4
    return pc, stack

def GetNewPos():
    x = pos[0]
    y = pos[1]
    if lastDirection == 1:
        y = y - 1
    if lastDirection == 2:
        y = y + 1
    if lastDirection == 3:
        x = x - 1
    if lastDirection == 4:
        x = x + 1
        
    if x < 0 or y < 0:
        return None
    if x >= width or y >= height:
        return None

    return [x,y]

def SetMazeObject(value):
    global maze
    place = GetNewPos()
    if place == None:
        return
    maze[place[1]][place[0]][0] = value
    
def Input(pc,stack,params):
    global maze
    global lastDirection
    global pos
   # DrawMaze()
    space = maze[pos[1]][pos[0]]
    value = space[1]
    lastDirection = value
    if space[1] == 5:
        if len(moves) == 0:
            return Halt(pc,stack,[])
        lastMove = moves.pop()
        stack = lastMove[0]
        pos = lastMove[1]
        return pc,stack
    space[1] = space[1] + 1
    SetValue(pc,stack,params,1,value)   
    pc = pc + 2
    clear()
    return pc, stack

def Output(pc,stack,params):
    global pos
    output = (GetValue(pc,stack,params,1))
    SetMazeObject(output)
    if not output == 0:
        updatePos = GetNewPos()
        if updatePos == None:
            print("Edge of array")
            return Halt(pc,stack,[])

        pos = updatePos
        moves.append([stack.copy(),pos.copy()])
    pc = pc + 2
    return pc, stack

def JumpIfTrue(pc,stack,params):
    if(GetValue(pc,stack,params,1) == 0):
        pc = pc + 3
        return pc,stack
    
    pc = GetValue(pc,stack,params,2)
    return pc,stack

def JumpIfFalse(pc,stack,params):
    if(GetValue(pc,stack,params,1) == 0):
        pc = GetValue(pc,stack,params,2)
        return pc,stack
    
    pc = pc + 3
    return pc,stack

def LessThan(pc,stack,params):
    part1 = GetValue(pc,stack,params,1)
    part2 = GetValue(pc,stack,params,2)
    if(part1 < part2):
        SetValue(pc,stack,params,3,1)
    else:
        SetValue(pc,stack,params,3,0)
    pc = pc + 4
    return pc,stack

def Equals(pc,stack,params):
    part1 = GetValue(pc,stack,params,1)
    part2 = GetValue(pc,stack,params,2)
    if(part1 == part2):
        SetValue(pc,stack,params,3,1)
    else:
        SetValue(pc,stack,params,3,0)
    pc = pc + 4
    return pc,stack

relativePos = 0

def AdjustRelative(pc,stack,params):
    global relativePos
    relativePos = relativePos + GetValue(pc,stack,params,1)
    pc = pc + 2
    return pc,stack
    
def Halt(pc,stack,params):
    pc = len(stack)
    return pc, stack


opcodes = [[1,Addition],
           [2,Multiply],
           [3,Input],
           [4,Output],
           [5,JumpIfTrue],
           [6,JumpIfFalse],
           [7,LessThan],
           [8,Equals],
           [9,AdjustRelative],
           [99,Halt]]

def RunProgram(memory):
    stack = memory.copy()
    pc = 0
    while(pc < len(stack)):
        data = stack[pc]
        strData = str(data)
        strData = "0" * (4 - len(strData)) + strData
        opcoded = int(strData[-2:])
        operand = strData[:-2][::-1]
        for opcode in opcodes:
            if(opcoded == opcode[0]):
                pc, stack = opcode[1](pc,stack,operand)
    return stack

filepath = 'input.txt'
file = open(filepath,"r")
inputData = file.read();

stack = inputData.replace("\n","").split(",")
for i in range(1000):
    stack.append("0")

RunProgram(stack)
pos = [int(width/2),int(height/2)]
for y in range(len(maze)):
    row = maze[y]
    for x in range(len(row)):
        row[x] = row[x][0]

foundExit = False
def FloodFill(x,y,depth):
    global maze
    global foundExit
    if foundExit:
        return
   # DrawMaze()

    if x < 0 or x >= width:
        return
    if y < 0 or y >= height:
        return
    if maze[y][x] == 0:
        return
    if maze[y][x] == 2:
        foundExit = True
        print(depth)
        return
    if maze[y][x] == 3:
        return
    maze[y][x] = 3

    FloodFill(x,y-1,depth+1)
    FloodFill(x+1,y,depth+1)
    FloodFill(x,y+1,depth+1)
    FloodFill(x-1,y,depth+1)

sys.setrecursionlimit(1500)
FloodFill(pos[0],pos[1],0)
DrawMaze()

