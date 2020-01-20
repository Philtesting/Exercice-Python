def inflation(s):
    mots = s.split()
    for i,m in enumerate(mots):
        if m.isnumeric():
            mots[i] = str(2*int(m))
    return " ".join(mots)
print(inflation("Le prix est 77 euros 30 cents"))