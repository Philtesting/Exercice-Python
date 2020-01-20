from re import findall

s = "Les 2 maquereaux valent 6,50 euros"

def nombres(s):
    motif = r"-?[0-9]+[,.]?[0-9]*"
    return(findall(motif,s))

print(nombres(s))