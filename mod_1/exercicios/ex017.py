import math
oposto = float(input('Digite o cateto oposto: '))
adj = float(input('Digite o cateto adjacente: '))
hipot = math.hypot(oposto, adj)
print(hipot)

#hipote = ((oposto * oposto) + (adj * adj)) ** (1/2)
#print(hipote)
