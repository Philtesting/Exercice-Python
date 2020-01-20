def voy(ch):
    
    nbVoy = (ch.count("a")+ch.count("e")+ch.count("i")+ch.count("o")+ch.count("u")+ch.count("A")+
         ch.count("E")+ch.count("I")+ch.count("O")+ch.count("U")+ch.count("Y")+ch.count("y"))
    
    return nbVoy

phrase = str(input("Donner moi une phrase:"))
print("Voici le nombre de voyelle:",voy(phrase))