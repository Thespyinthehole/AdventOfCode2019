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

opcodes = [[1,Addition],[2,Multiply],[99,Halt]]

def RunProgram(memory):
    stack = memory.copy()
    pc = 0
    while(pc < len(stack)):
        data = stack[pc]
        for opcode in opcodes:
            if(data == opcode[0]):
                pc, stack = opcode[1](pc,stack)
    return stack

filepath = 'input.txt'
file = open(filepath,"r")
inputData = file.read();

stack = inputData[:-1].split(",")
for i in range(len(stack)):
    stack[i] = int(stack[i])

def CheckNounVerb(noun,verb):   
    stack[1] = noun
    stack[2] = verb

    result = RunProgram(stack)


    return (result[0])

for i in range(100):
    for o in range(100):
        answer = CheckNounVerb(i,o)

        if (answer == 19690720):
            print("[" + str(i) + ", " + str(o) + "] -> " + str(answer))
            print("Result: " + str(100 * i + o))
            quit
