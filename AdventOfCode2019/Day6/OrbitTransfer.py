filepath = 'input.txt'
file = open(filepath,"r")
orbits = file.read();

orbits = orbits[:-1].split("\n")
orbitals = []

def CalculateOrbitalNumber(orbital):
    for orbit in orbitals:
        if orbital.parent == orbit.name:
            return 1 + CalculateOrbitalNumber(orbit)
    
    return 1

class Orbital:
    def __init__(self,name,parent):
        self.name = name
        self.parent = parent

    def __str__(self):
        return self.name + " orbits " + self.parent

    def __repr__(self):
        return str(self)
    
for i in range(len(orbits)):
    orbits[i] = orbits[i].split(")")
    orbit = Orbital(orbits[i][1],orbits[i][0])
    orbitals.append(orbit)


def GetOrbital(name):
    for orbit in orbitals:
        if(orbit.name == name):
            return orbit

you = GetOrbital("YOU")
target = GetOrbital("SAN")
total = 0

commonAncester = ""
youtotal = 0
while not you.parent == "":
    parent = GetOrbital(you.parent)
    if parent == None:
        break
    you.parent = parent.parent
    youtotal = youtotal + 1
    targettotal = 0
    targetParent = target.parent
    while not target.parent == "":
        if target.parent == you.parent:
            commonAncester = you.parent
            total = youtotal + targettotal
            break
        
        targettotal = targettotal + 1
        tarparent = GetOrbital(target.parent)
        if tarparent == None:
            target.parent = targetParent
            break
        target.parent = tarparent.parent
        
    target.parent = targetParent
    if not commonAncester == "":
        break
    
print(total)





