datam = "153517-630395"
data = datam.split("-");

start = int(data[0])
end = int(data[1])

total = 0
for i in range(start,end):
    value = str(i)
    double = False
    increasing = True
    usedNums = []
    for o in range(len(value)):
        if(o == len(value)-1):
            continue
        if value[o] == value[o+1] and not int(value[o]) in usedNums:
            usedNums.append(int(value[o]))
            more = False
            for p in range(o+2,len(value)):
                if (value[o] == value[p]):
                    more = True
                    break
            if not more:
               double = True

        if(int(value[o]) > int(value[o+1])):
            increasing = False
    if not double:
        continue
    if not increasing:
        continue
    total = total + 1
    
print("Total: " + str(total))
