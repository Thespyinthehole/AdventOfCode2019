from itertools import permutations

def GetValue(pc,stack,parameters,i):
    if(i-1 < len(parameters)):
        if(parameters[i-1] == '1'):
            return int(stack[pc+i])
    return int(stack[int(stack[pc+i])])

def SetValue(pc,stack,i,value):
    stack[int(stack[pc+i])] = str(value)
    
def Addition(pc,stack,params):
    part1 = GetValue(pc,stack,params,1)
    part2 = GetValue(pc,stack,params,2)
    value = part1 + part2

    SetValue(pc,stack,3,value)
    pc = pc + 4
    return pc, stack

def Multiply(pc,stack,params):
    part1 = GetValue(pc,stack,params,1)
    part2 = GetValue(pc,stack,params,2)
    value = part1 * part2

    SetValue(pc,stack,3,value)
    pc = pc + 4
    return pc, stack


data = ["0"]

def Input(pc,stack,params):
    value = data.pop()#input("Enter an integer: ") 
    SetValue(pc,stack,1,value)   
    pc = pc + 2
    return pc, stack

def Output(pc,stack,params):
    data.append(str(GetValue(pc,stack,params,1)))
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
        SetValue(pc,stack,3,1)
    else:
        SetValue(pc,stack,3,0)
    pc = pc + 4
    return pc,stack

def Equals(pc,stack,params):
    part1 = GetValue(pc,stack,params,1)
    part2 = GetValue(pc,stack,params,2)
    if(part1 == part2):
        SetValue(pc,stack,3,1)
    else:
        SetValue(pc,stack,3,0)
    pc = pc + 4
    return pc,stack

halt = False
def Halt(pc,stack,params):
    pc = len(stack)
    halt = True
    return pc, stack


opcodes = [[1,Addition],
           [2,Multiply],
           [3,Input],
           [4,Output],
           [5,JumpIfTrue],
           [6,JumpIfFalse],
           [7,LessThan],
           [8,Equals],
           [99,Halt]]

def RunProgram(memory):
    stack = memory.copy()
    pc = 0
    while(pc < len(stack)):
        data = stack[pc]
        strData = str(data)
        opcoded = int(strData[-2:])
        operand = strData[:-2][::-1]
        for opcode in opcodes:
            if(opcoded == opcode[0]):
                pc, stack = opcode[1](pc,stack,operand)
    return stack

filepath = 'input.txt'
file = open(filepath,"r")
inputData = """3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"""#file.read();
settings = "9,8,7,6,5"
settings = settings.split(",")
#settings = list(permutations(settings))
#print(settings)
stack = inputData.replace("\n","").split(",")
amplifiers = [stack.copy() for i in range(5)]
maximum = 0

i = 0
while not halt:
    print(data)

    data.append(settings[i])
    amplifiers[i] = RunProgram(amplifiers[i])
    i = i + 1
    if i == 5:
        i = 0
