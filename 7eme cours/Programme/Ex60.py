def hascap(s):
    mots = s.split()
    majs = []
    for m in mots:
        if m[0].isupper():
            majs.append(m)
    return majs
print(hascap("Il était une fois, Jean François"))