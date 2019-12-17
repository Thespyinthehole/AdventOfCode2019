import math
from pprint import *
filename = "input.txt"
file = open(filename)
data = file.read()[:-1]

class Ingredient:
    def __init__(self, material, amount):
        self.material = material
        self.amount = amount

    def __str__(self):
        return self.material + ": " + str(self.amount)

    def __repr__(self):
        return str(self)
    
class Recipe:
    def __init__(self,array):
        ins = array[0]
        outs = array[1][0]
        self.materials = []
        for i in ins:
            self.materials.append(Ingredient(i[1],int(i[0])))
        self.output = Ingredient(outs[1],int(outs[0]))

    def __str__(self):
        string = str(self.output)
        for material in self.materials:
            string = string + "\n   " + str(material)
        return string
    
    def __repr__(self):
        return str(self)
    
data = data.split("\n")
for i in range(len(data)):
    datam = data[i]
    datam = datam.split(" => ")
  
    for o in range(len(datam)):
        part = datam[o]
        part = part.split(", ")
        for p in range(len(part)):
            part[p] = part[p].split(" ")
        datam[o] = part
    data[i] = datam
  
recipes = []
index = 0
for datam in data:
    recipes.append(Recipe(datam))
    if recipes[-1].output.material == "FUEL":
        index = len(recipes)-1

fuelRecipe = recipes[index]
    
stuffGot = []

for recipe in recipes:
    stuffGot.append(Ingredient(recipe.output.material,0))
    #print(recipe)
    #print()
    

def IndexOf(stuff):
    for got in stuffGot:
        if got.material == stuff:
            return stuffGot.index(got)
    return -1

def AmountOf(stuff):
    index = IndexOf(stuff)
    if index == -1:
        return 0
    return stuffGot[index].amount

def GetRecipe(stuff):
    for recipe in recipes:
        if recipe.output.material == stuff:
            return recipe
    return None

usedOre = 0
def MakeMore(stuff,amount):
    global usedOre
    global stuffGot
    
    recipe = GetRecipe(stuff)
    times = math.ceil(amount/recipe.output.amount)
    
    for mat in recipe.materials:
        if mat.material == "ORE":
            usedOre = usedOre + mat.amount * times
            continue
        while AmountOf(mat.material) < mat.amount * times:
            MakeMore(mat.material, mat.amount*times-AmountOf(mat.material))

        #Uses materials
        index = IndexOf(mat.material)
        stuffGot[index].amount = stuffGot[index].amount - mat.amount * times

    #Get materials
    mainIndex = IndexOf(recipe.output.material)
    stuffGot[mainIndex].amount = stuffGot[mainIndex].amount + recipe.output.amount * times

target = 1000000000000
lower = 0
upper = target

while not usedOre == target:
    usedOre = 0
    for i in stuffGot:
        i.amount = 0
    mid = round((lower + upper)/2)
    MakeMore("FUEL",mid)
    print("Ore used by " + str(mid) + ": " + str(usedOre))
    if usedOre > target:
        upper = mid
    else:
        lower = mid
    input()
