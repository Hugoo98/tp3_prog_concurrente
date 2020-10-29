
#!/usr/bin/python
import time


#Exercice_1:
def compte_mots(phrase):

    return len(phrase.split())



#Exercice_2:

def replace_multiple1(s1, s2, n):
    l1 = list(s1)
    l2 = list(s2)

    step = int((len(l1) - 1) / n) + 1

    i = 0
    for i in range(1, step):
        l1[i * n] = l2[i - 1]

    length2 = len(l2)
    if length2 > i:
        l1.extend(l2[i:length2])

    return "".join(l1)

def remplace_multiple2(s1,s2,n):
    s=s1
    n1=n
    for i in range (2,len(s2)+1):
        s=s[0:n]+s2[i-2]+s[n+1:len(s1)+1]
        n=n1
        n*=i
        if(n>len(s1)):
            return s+s2[(i-1):len(s2)+1]
    return s

#Exercice_3:

#Enoncé_1:
def termeU(n):
    if(n == 0):
        return 1
    elif(n >= 1):
        return termeU(n-1) * pow(2,n) + n

#Enoncé_2:
def serie(p):
    i=0
    s=0
    while i<=p:
        s = s + termeU(i)
        i = i+1
    return s
#Enoncé_3:


#Enoncé_4:


#Exercice_5

#version fonctionnelle
def fact1(n):
    if n == 0 :
        return 1
    if n == 1:
        return 1
    else:
        return n * fact1(n-1)

#version non fonctionnelle
def fact2(n):
    a = 1
    for i in range(2, n + 1):
        a *= i
    return a


if __name__ == '__main__':
#exo_1
    print(compte_mots(("")))
    print(compte_mots(("il ingurgite impunément uniguane.")))
    print(compte_mots(("coursdeprogrammation")))
    print(compte_mots(("hsdyzag zeskehgseufu wdkfjshi skdjfh kdsjn kehb")))

#exo_2
    test1 = replace_multiple1('', '', 2)
    test2 = replace_multiple1('abacus', 'oiseau', 2)
    test3 = replace_multiple1('hirondelles', 'nid', 3)
    print(test1, test1 == '')
    print(test2, test2 == 'abocisseau')
    print(test3, test3 == 'hirnndillds')

    print(remplace_multiple2('', '', 2))
    print(remplace_multiple2('abacus', 'oiseau', 2))
    print(remplace_multiple2('melahi', 'tachour', 3))
#Exo_3
##Enoncé 1

    print(termeU(0))
    print(termeU(1))
    print(termeU(5))
    print(termeU(10))

##Enoncé 2
    print(serie(0))
    print(serie(1))
    print(serie(5))
    print(serie(10))

#Enoncé_3
#Enoncé_4
#Enoncé_5
    """
# measure process time
    t0 = time.clock()
    serie(100)
    print (time.clock(), "seconds process time")
    """


#Exo_4
    print(fact1(1))
    print(fact1(2))
    print(fact1(3))
    print(fact1(4))


    print(fact2(1))
    print(fact2(2))
    print(fact2(3))
    print(fact2(4))

