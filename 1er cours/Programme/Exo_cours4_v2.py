
l = ''
c = ''
p = 1
e = ' ' * 10

for i in range(10):
  e = e[0:10-i]
  c = ''
  for j in range(p):
    c += chr(174)
  l += e+c+'\n'
  p += 2

f = ' ' * 8

for i in range(4):
    c = ''
    c +=  chr(174) * 5
    l += f+c+'\n'
print(l)
    
    
    