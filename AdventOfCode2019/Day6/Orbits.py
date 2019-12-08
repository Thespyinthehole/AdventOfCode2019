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
        return self.name

    def __repr__(self):
        return str(self)
    
for i in range(len(orbits)):
    print(orbits[i])
    orbits[i] = orbits[i].split(")")
    orbit = Orbital(orbits[i][1],orbits[i][0])
    orbitals.append(orbit)


total = 0
for orbit in orbitals:
    total = total + CalculateOrbitalNumber(orbit)

print(total)
