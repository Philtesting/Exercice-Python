
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


x= (12.8 * 4 + 9.67 * 4)
y= (15 * 2) + (9.5 * 2)

for z in range_positve(0.0,10.0,0.1):
    totale = (x + y + (z*18)) / 30 + 0.318
    if totale >= 10:
        print ("%g " % z)
        print ("%g " % totale)
        break

for a in range_positve(0.0,10,0.1):
        c = 15
        b = 9
        tot = (a * 8 + b * 6 + c * 4) / 16
        if tot >= 8.5:
            print (f'{a} + {b} + {c}')
            totale = (x + y + (tot*18)) / 30 + 0.318
            print(totale)
            



