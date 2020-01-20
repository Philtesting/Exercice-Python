liste1 = [1,2,3,4,5]
m = len(liste1)
found = False
while m>0 and not found:
    for i in range(len(liste1)-m):
        if liste1[i:i+m] == liste1[i+m-1:i-1:-1]:
            found = True
            result = liste1[i:i+m]
    m -= 1
print(result)