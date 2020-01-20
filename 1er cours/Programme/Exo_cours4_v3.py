l = ''
c = ''
p = 1
N= int(input("Choisissez la hauteur:"))
e = ' ' * N

for i in range(N):
  e = e[0:N-i]
  c = ''
  for j in range(p):
    c += chr(174)
  l += e+c+'\n'
  p += 2

f = ' ' * (N-2)

for i in range(4):
    c = ''
    c +=  chr(174) * 5
    l += f+c+'\n'
print(l)
    
    
    