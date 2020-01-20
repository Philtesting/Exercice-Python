c2 ="Votez pour moi"
a = c2.split()
print(a)
c4 ="Cet exemple, parmi d'autres, peut encore servir"
print(c4.split(","))

b2 = ["Salut","les","copains"]
print (" ".join(b2))
print ("---".join(b2))

ch1 = "Cette leçon vaut bien un fromage, sans doute ?"
ch2 = "fromage"
print (ch1.find(ch2))

ch1 = "Le héron au long bec emmanché d'un long cou"
ch2 = 'long'
print (ch1.count(ch2))

ch ="ATTENTION : Danger !"
print (ch.lower())

ch = "Merci beaucoup"
print (ch.upper())

b3 = "quel beau temps, aujourd'hui !"
print (b3.capitalize())

ch5 = "La CIGALE et la FOURMI"
print (ch5.swapcase())

ch = "    Monty Python    "
print(ch.strip())

ch8 = "Si ce n'est toi c'est donc ton frère"
print( ch8.replace(" ","*"))

ch9 ="Portez ce vieux whisky au juge blond qui fume"
print (ch9.index("w"))

print (ch9.index("e"))
print (ch9.index("e",5))
print (ch9.index("e",15))

a = float("12.36")
print (a + 5)

a = int("184")
print (a + 20)

