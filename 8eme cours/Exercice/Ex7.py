l,c,p,e = '','',1,' ' * 10

for i in range(10):
  e = e[0:10-i] * 2
  c = ''
  for j in range(p):
    c += ":)"
  l += e+c+'\n'
  p += 2

f = ' ' * 8

for i in range(4):
    c = ''
    c +=  ":)" * 5
    l += f * 2+c+'\n'
print(l)
    
    
    
