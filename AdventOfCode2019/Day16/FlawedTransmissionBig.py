from math import *
from timeit import default_timer as timer
import cProfile

filename = "input.txt"
file = open(filename,"r")

inputSignal = file.read()[:-1]#"19617804207202209144916044189917"
basePattern = [0,1,0,-1]

phases = 1
digits = len(inputSignal)
signalLength = digits * 10000

def UpdateDigit(digit):
    digitPattern = []
    patternLength = 4 * digit + 4
    for o in basePattern:
        digitPattern.extend([o]*(digit+1))
    start = digitPattern[0]
    digitPattern = digitPattern[1:]
    digitPattern.append(start)

    signal = inputSignal
    digitsToAdd = patternLength-digits
    length = digits
    if digitsToAdd > 0:
        for p in range(digitsToAdd):
            pos = p % digits
            nextChr = inputSignal[pos]
            signal = signal + nextChr
        length = patternLength

    total = 0
    for c in range(length):
        value = int(signal[c])
        offset = digitPattern[c % patternLength]
        total = total + value * offset
            
    used = floor(signalLength / length) * length
    remaining = signalLength - used
    startOffset = used-floor(used / digits) * digits
    for c in range(remaining):
        pos = (startOffset + c) % digits
        value = int(inputSignal[pos])
        offset = digitPattern[c % length]
        total = total + value * offset
        
    return abs(total) % 10

def AddString(string,value,i):
    return string[:i] + str(value) + string[i+1:]

def RunPhase():
    global inputSignal
    outputSignal = "0" * digits
    for digit in range(digits):
        total = UpdateDigit(digit)
        outputSignal = AddString(outputSignal,total,digit)
    inputSignal = outputSignal


def RunPhases():
    for i in range(phases):    
        RunPhase()
        
cProfile.run('RunPhases()')

offset = int(inputSignal[:8])
print(offset)
#inputSignal = inputSignal * 10000
#print(inputSignal[offset:offset+9])
