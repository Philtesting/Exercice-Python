l = [1,7,3,7,5]
n=0
l.append(6)
for i in l:
    if (i == 7):
        n+=1
if n==0:
    print("pas  trouver")
else:
    print("7 aparait:",n,"fois")

sum = 0   
x = 0

while x < len(l):
    sum += l[x]
    x+=1
moy = sum/len(l)
print("%2.2f"%(moy))
sum = 0
for j in l:
    sum += j
moy = sum/len(l)
print("%2.2f"%(moy))

alpha ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = alpha[5:-1]
print(s)
s = alpha[-5:24]
print(s)
s = alpha[-5:-1]
print(s)

    
