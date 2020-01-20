n=[]

for i in range(10):
    x = float(input("Note:"))
    n.insert(i,x)
print(n)

moy = sum(n) / 10

print("Moyenne :",moy)

M = max(n)
m = min(n)
a= M - moy
b= m - moy

for i in range(10):
    n[i] = n[i] - moy

MOY = sum(n) / 10

print("Note la plus haute:",M)
print("Note la plus basse:",m)
print("Ecart entre le max et la moyenne:",a)
print("Ecart entre le min et le moyenne:",b)
print("Ecart moyen entre les notes fournis et la moyenne:",MOY)

        
         



   