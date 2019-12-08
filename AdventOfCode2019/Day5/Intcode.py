def GetValue(pc,stack,parameters,i):
    #print(i)
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
  #  print(str(part1) + " + " + str(part2) + " = " + str(value))
    SetValue(pc,stack,3,value)
    pc = pc + 4
    return pc, stack

def Multiply(pc,stack,params):
    part1 = GetValue(pc,stack,params,1)
    part2 = GetValue(pc,stack,params,2)
    value = part1 * part2
    #print(str(part1) + " * " + str(part2) + " = " + str(value))
    SetValue(pc,stack,3,value)
    pc = pc + 4
    return pc, stack

def Input(pc,stack,params):
    value = input("Enter an integer: ") 
    SetValue(pc,stack,1,value)   
    pc = pc + 2
    return pc, stack

def Output(pc,stack,params):
    print(GetValue(pc,stack,params,1))
    pc = pc + 2
    return pc, stack

def Halt(pc,stack,params):
    pc = len(stack)
    return pc, stack


opcodes = [[1,Addition],[2,Multiply],[3,Input],[4,Output],[99,Halt]]

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
inputData = file.read();

stack = inputData[:-1].split(",")

print(RunProgram(stack))
