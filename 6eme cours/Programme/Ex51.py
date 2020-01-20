def phrase(s):
    mots = ['']
    for i in s:
        if i ==' ':
            mots.append('')
        else :
            mots[-1] += i
    return mots
print(phrase('Bonjour les enfants'))