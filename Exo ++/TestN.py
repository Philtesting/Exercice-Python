
def range_positve(start, stop=None, step=None):
    if stop == None:
        stop = start + 0.0
        start = 0.0
    if step == None:
        step = 1.0
    while start < stop:
        yield start
        start += step

def range_positve(start, stop=None, step=None):
    if stop == None:
        stop = start + 0.0
        start = 0.0
    if step == None:
        step = 1.0
    while start < stop:
        yield start
        start += step


x= (14.5*4 + 13.8*2)
y= (12 * 4) + (13.5 * 4)

for z in range_positve(0.0,10.0,0.1):
    totale = (x + y + (z*16)) / 30 + 0.4
    if totale >= 10:
        print ("%g " % z)
        print ("%g " % totale)
        break

for b in range_positve(0.0,10,0.1):
    a = 7
    c = 4
    tot = (a * 6 + b * 6 + c * 4) / 16
    if tot >= 6.3:
        print (f'{a} + {b} + {c}')
        break


