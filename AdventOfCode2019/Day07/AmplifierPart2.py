from itertools import permutations


class IntComputer:
    def __init__(self,stack,inputData):
        self.inStream = inputData
        self.outStream = []
        self.pc = 0
        self.stack = stack
        
    def GetValue(self,parameters,i):
        if(i-1 < len(parameters)):
            if(parameters[i-1] == '1'):
                return int(self.stack[self.pc+i])
        return int(self.stack[int(self.stack[self.pc+i])])

    def SetValue(self,i,value):
        self.stack[int(self.stack[self.pc+i])] = str(value)

    def PcCount(self,i):
        self.pc = self.pc + i
        
    def Addition(self,params):
        part1 = self.GetValue(params,1)
        part2 = self.GetValue(params,2)
        value = part1 + part2

        self.SetValue(3,value)
        self.PcCount(4)

    def Multiply(self,params):
        part1 = self.GetValue(params,1)
        part2 = self.GetValue(params,2)
        value = part1 * part2

        self.SetValue(3,value)
        self.PcCount(4)

    def Input(self,params):
        if len(self.inStream) == 0:
            self.waiting = True
            return
        value = self.inStream.pop()#input("Enter an integer: ") 
        self.SetValue(1,value)
        self.PcCount(2)

    def Output(self,params):
        data = self.GetValue(params,1)
        self.outStream.append(str(data))
        self.PcCount(2)

    def JumpIfTrue(self,params):
        cmp = self.GetValue(params,1)
        if(cmp == 0):
            self.PcCount(3)
            return 
        
        self.pc = self.GetValue(params,2)

    def JumpIfFalse(self,params):
        cmp = self.GetValue(params,1)
        if(cmp == 0):
            self.pc = self.GetValue(params,2)
            return 

        self.PcCount(3)

    def LessThan(self,params):
        part1 = self.GetValue(params,1)
        part2 = self.GetValue(params,2)
        if(part1 < part2):
            self.SetValue(3,1)
        else:
            self.SetValue(3,0)
        self.PcCount(4)

    def Equals(self,params):
        part1 = self.GetValue(params,1)
        part2 = self.GetValue(params,2)
        if(part1 == part2):
            self.SetValue(3,1)
        else:
            self.SetValue(3,0)
        self.PcCount(4)

    def Halt(self,params):
        self.pc = len(self.stack)
        self.halt = True

    halt = False
    waiting = False
    opcodes = [[1,Addition],
               [2,Multiply],
               [3,Input],
               [4,Output],
               [5,JumpIfTrue],
               [6,JumpIfFalse],
               [7,LessThan],
               [8,Equals],
               [99,Halt]]

    def RunProgram(self):
        self.waiting = False
        while(self.pc < len(self.stack)):
            data = self.stack[self.pc]
            strData = str(data)
            strData = "0" * (4-len(strData)) + strData
            opcoded = int(strData[-2:])
            operand = strData[:-2][::-1]
            for opcode in self.opcodes:
                if(opcoded == opcode[0]):
                    opcode[1](self,operand)
            if self.waiting:
                return
            
filepath = 'input.txt'
file = open(filepath,"r")
inputData = file.read();
settings = "9,7,8,5,6"
settings = settings.split(",")
settings = list(permutations(settings))
#print(settings)
stack = inputData.replace("\n","").split(",")

maximum = 0
for setting in settings:
    amplifiers = []
    amplifiers.append(IntComputer(stack.copy(),[]))
    for i in range(1,5):
        lastOut = amplifiers[i-1].outStream
        amplifiers.append(IntComputer(stack.copy(),lastOut))

    amplifiers[0].inStream = amplifiers[4].outStream

    amplifiers[0].inStream.append("0")

    i = 0
    halted = 0
    first = True
    while halted < 5:
        if first:
            amplifiers[i].inStream.append(setting[i])
        amplifiers[i].RunProgram()
        
        if amplifiers[i].halt:
            halted = halted + 1
        i = i + 1
        if i == 5:
            i = 0
            first = False

    value = int(amplifiers[4].outStream[0])
    if value > maximum:
        maximum = value

print(maximum)
