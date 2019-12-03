
def Addition(pc,stack):
    stack[stack[pc+3]] = stack[stack[pc+2]] + stack[stack[pc+1]]
    pc = pc + 4
    return pc, stack

def Multiply(pc,stack):
    stack[stack[pc+3]] = stack[stack[pc+2]] * stack[stack[pc+1]]
    pc = pc + 4
    return pc, stack

def Halt(pc,stack):
    pc = len(stack)
    return pc, stack

pc = 0
opcodes = [[1,Addition],[2,Multiply],[99,Halt]]

filepath = 'input.txt'
file = open(filepath,"r")
inputData = file.read();

stack = inputData[:-1].split(",")
for i in range(len(stack)):
    stack[i] = int(stack[i])
stack[1] = 12
stack[2] = 2

while(pc < len(stack)):
    data = stack[pc])
    for opcode in opcodes:
        if(data == opcode[0]):
            pc, stack = opcode[1](pc,stack)

print(stack)
