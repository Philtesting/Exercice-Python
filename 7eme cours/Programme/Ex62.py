from re import *
def tronc(s):
    motif = r"(-?)([0-9]+)[,.]?[0-9]*"
    return sub(motif, r"\1\2", s)
s = "L'evolution sur 3,5 jours est de -7.23 points"
print(tronc(s))