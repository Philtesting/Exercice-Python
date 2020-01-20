a = [ 2 * i for i in range (1,16)]
b = [ 3 * i for i in range (1,16)]
c = [ 5 * i for i in range (1,16)]
d = [ 7 * i for i in range (1,16)]
e = [ 11 * i for i in range (1,16)]
f = [ 13 * i for i in range (1,16)]
g = [ 17 * i for i in range (1,16)]
h = [ 19 * i for i in range (1,16)]
som = a + b + c + d + e + f + g + h
for y in range(0,16*8+1,15):
    print ( ' '.join(str(x) for x in som[y:y+15]),"\n")
