nombres = [17, 38, 10, 25, 72]
nombres.sort()             
print(nombres)

nombres.append(12)         
print(nombres)

nombres.reverse()          
print(nombres)

print(nombres.index(17))

nombres.remove(38)         
print(nombres)

del nombres[2]
print(nombres)

del nombres[1:3]
print(nombres)