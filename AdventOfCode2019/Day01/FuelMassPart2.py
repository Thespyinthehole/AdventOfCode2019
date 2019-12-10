from math import *

def CalculateFuel(mass):
    fuel = floor(mass / 3) - 2
    if(fuel <= 0):
        return 0
    return fuel + CalculateFuel(fuel)

filepath = 'input.txt'
totalFuel = 0
with open(filepath) as fp:
   line = fp.readline()
   while line:
       mass = int(line)
       totalFuel = totalFuel + CalculateFuel(mass)
       line = fp.readline()


print(totalFuel)

