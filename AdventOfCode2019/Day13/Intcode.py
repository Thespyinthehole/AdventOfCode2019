from graphics import *

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
    value = input("Enter an integer: ") 
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
total = 0
for i in range(0,len(data),3):
    x = data[i]
    y = data[i+1]
    tile = data[i+2]
    if tile == 0:
        continue
    if tile == 2:
        total = total + 1
print(total)
