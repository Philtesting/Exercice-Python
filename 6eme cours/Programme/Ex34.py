from Ex30 import *

def combinaisons(n,p):
    return ( factorielle(n) // (factorielle(p)*factorielle(n-p)))