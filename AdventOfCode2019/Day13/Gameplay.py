from graphics import *
import time

win = GraphWin("Ball Game",400,400, autoflush=False)
gameBoard = [[0 for x in range(38)].copy() for y in range(22)]
ballPos = [0,0]
batPos = [0,0]

def clear():
    for item in win.items[:]:
        item.undraw()
    win.update()

def DrawBoard():
    for x in range(38):
        for y in range(22):
            tile = gameBoard[y][x]
            color = 'white'
            if tile == 0:
                continue
            if tile == 1:
                color = 'blue'
            if tile == 2:
                color = 'red'
            if tile == 3:
                color = 'green'
            if tile == 4:
                color = 'yellow'
            size = 10
            pt1 = Point(x*size,y*size)
            pt2 = Point(x*size+size,y*size+size)
            rec = Rectangle(pt1,pt2)
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

def Input(pc,stack,params):
    global batPos
    global ballPos
    DrawBoard()
    value = 0
    if batPos[0] > ballPos[0]:
        value = -1
    elif batPos[0] < ballPos[0]:
        value = 1
    time.sleep(0.1)
    clear()
    SetValue(pc,stack,params,1,value)   
    pc = pc + 2
    return pc, stack

data = []
def Output(pc,stack,params):
    data.append(GetValue(pc,stack,params,1))
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


score = 0

def RunProgram(memory):
    global data
    global ballPos
    global batPos
    global score
    stack = memory.copy()
    pc = 0
    xs = 0
    while(pc < len(stack)):
        output = stack[pc]
        strData = str(output)
        strData = "0" * (4 - len(strData)) + strData
        opcoded = int(strData[-2:])
        operand = strData[:-2][::-1]
        for opcode in opcodes:
            if(opcoded == opcode[0]):
                pc, stack = opcode[1](pc,stack,operand)

        if not len(data) % 3 == 0:
            continue
        for i in range(0,len(data),3):
            x = data[i]
            y = data[i+1]
            tile = data[i+2]
            if x == -1:
                score = tile
                continue

            if tile == 3:
                batPos[0] = x
                batPos[1] = y

            if tile == 4:
                ballPos[0] = x
                ballPos[1] = y

            gameBoard[y][x] = tile
        data = []
    return stack

filepath = 'input.txt'
file = open(filepath,"r")
inputData = file.read();

stack = inputData.replace("\n","").split(",")
for i in range(1000):
    stack.append("0")
    
RunProgram(stack)
print(score)
