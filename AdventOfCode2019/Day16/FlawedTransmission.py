filename = "input.txt"
file = open(filename,"r")

inputSignal = "12345678"#file.read()[:-1]#"19617804207202209144916044189917"
inputSignal = inputSignal
basePattern = [0,1,0,-1]

phases = 1
digits = len(inputSignal)
for i in range(phases):
    outputSignal = "0" * digits
    for digit in range(digits):
        digitPattern = []
        for o in basePattern:
            digitPattern.extend([o]*(digit+1))
        start = digitPattern[0]
        digitPattern = digitPattern[1:]
        digitPattern.append(start)
        total = 0
        for c in range(digits):
            value = int(inputSignal[c])
            offset = digitPattern[c % len(digitPattern)]
            total = total + value * offset
            #print(str(value) + "*" + str(offset),end=" ")
        total = abs(total) % 10
        #print(" = " + str(total))
        outputSignal = outputSignal[:digit] + str(total) + outputSignal[digit+1:]
    inputSignal = outputSignal

print(inputSignal[:8])
