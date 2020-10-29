
#Exercice 1:
def compte_mots(phrase):

    return len(phrase.split())



#Exercice 2:

def replace_multiple(s1,s2,n):


    for i in range(len(s1)//(n+1)):
        if(s1!='' and s2!='' ):
            if(i==0):
                s = (s1.replace(s1[n], s2[0]))
            if(i>=n):
                s = (s1.replace(s1[i * n], s2[i]))
    print(s + s2[2 : len(s2)]);


#Exercice 3:

#Enoncé 1:
def termeU(n):
    if(n == 0):
        return 1
    elif(n >= 1):
        return termeU(n-1) * pow(2,n) + n

#Enoncé 2:
def serie(p):
    i=0
    s=0

    while i<=p:
        s = s + termeU(i)
        i = i+1
    return s
#Enoncé 3:

#Enoncé 4:


if __name__ == '__main__':
    print(compte_mots(("")))
    print(compte_mots(("il ingurgite impunément uniguane.")))
    print(compte_mots(("coursdeprogrammation")))
    print(compte_mots(("Attention aux espaces consécutifs ou terminaux")))

    replace_multiple('melahi','tachour',2)

    print(termeU(0))
    print(termeU(1))
    print(termeU(5))
    print(termeU(10))

    print(serie(0))
    print(serie(1))
    print(serie(5))
    print(serie(10))
