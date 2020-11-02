
#!/usr/bin/python
from time import process_time


#Exercice_1:
def compte_mots(phrase):

    return len(phrase.split())



#Exercice_2:

def replace_multiple(s1, s2, n):
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
def serie_v2(p):
    u=1
    s=1
    i=1
    while(i<=p):
        u=u*(2**i)+i
        s=s+u
        i = i+1
    return s


#Enoncé_4:
"""
                 i              u                       s
--------------------------------------------------------------------
|Iteration 0 |  i=1   |  u=1                |   s=1                |   
-------------------------------------------------------------------------------
|Iteration 1 |   1    |  3                  |   4                  |  i+=1 =2 |
-------------------------------------------------------------------------------
|Iteration 2 |   2    |  14                 |   18                 |  i=3     |
-------------------------------------------------------------------------------
|Iteration 3 |   3    |  115                |   133                |  i=4     |
-------------------------------------------------------------------------------
|Iteration 4 |   4    |  1844               |   1977               |  i=5     |
-------------------------------------------------------------------------------
|Iteration 5 |   5    |  59013              |   60990              |  i=6     |
-------------------------------------------------------------------------------
|Iteration 6 |   6    |  3776828            |   3837828            |  i=7     |
-------------------------------------------------------------------------------
|Iteration 7 |   7    |  483435271          |   487273099          |  i=8     |
-------------------------------------------------------------------------------
|Iteration 8 |   8    |  123759429384       |   124246702483       |  i=9     |
-------------------------------------------------------------------------------
|Iteration 9 |   9    |  63364827844617     |   63489074547100     |  i=10    |
-------------------------------------------------------------------------------
|Iteration 10|   10   |  64885583712887818  |   64949072787434918  |
--------------------------------------------------------------------
"""
#Enoncé_5

#Après qu'on a mesuré le temps d'execution de la fonction serie() et serie_v2() (dans le main)
# on trouve que :
# le temps d'exécution de la fonction serie() > temps d'execution de la fonction serie_v2().
#Ce que veut dire: l'algorithme le plus efficace est serie_v2.

#Exercice_4

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
    a5="\nRésultat de la fonction compte_mots :\n"
    print(a5)
    print(compte_mots(("")))
    print(compte_mots(("il ingurgite impunément uniguane.")))
    print(compte_mots(("coursdeprogrammation")))
    print(compte_mots(("hsdyzag zeskehgseufu wdkfjshi skdjfh kdsjn kehb")))

#exo_2
    a4="\nRésultat de la fonction replace_multiple :\n"
    print(a4)
    test1 = replace_multiple('', '', 2)
    test2 = replace_multiple('abacus', 'oiseau', 2)
    test3 = replace_multiple('hirondelles', 'nid', 3)
    print(test1, test1 == '')
    print(test2, test2 == 'abocisseau')
    print(test3, test3 == 'hirondilles')
#Exo_3
##Enoncé 1
    a1="\nRésultats de la fonction termeU :\n"
    print(a1)
    print(termeU(0))
    print(termeU(1))
    print(termeU(5))
    print(termeU(10))

##Enoncé 2
    a2 = "\nRésultats de la fonction serie  :\n"
    print(a2)

    print(serie(0))
    print(serie(1))
    print(serie(5))
    print(serie(10))

#Enoncé_3
    a3 = "\nRésultats de la fonction serie_v2:\n"
    print(a3)
    print(serie_v2(0))
    print(serie_v2(1))
    print(serie_v2(5))
    print(serie_v2(10))


#Enoncé_5
    a6 = "\nRésultats de comparaison entre le temp d'exécution de la fonction serie et serie_v2 :\n"
    print(a6)

    x=100
    t1_start = process_time()
    print("serie(",x,") : ",serie(x))
    t1_stop = process_time()
    print("temps passe en secondes : ", t1_stop - t1_start )
    print("\n")
    t1_start = process_time()
    print("serie_v2(",x,") : ",serie_v2(x))
    t1_stop = process_time()
    print("temps passe en secondes : ", t1_stop - t1_start )


#Exo_4
    a="\nrésultats de la fonction factorielle(version fonctionnelle) :\n"
    b="\nrésultats de la fonction factorielle(version non fonctionnelle) :\n"
    print(a)
    print(fact1(1))
    print(fact1(2))
    print(fact1(3))
    print(fact1(4))


    print(b)
    print(fact2(1))
    print(fact2(2))
    print(fact2(3))
    print(fact2(4))

