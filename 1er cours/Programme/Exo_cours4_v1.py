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
print(l)
    
    
    