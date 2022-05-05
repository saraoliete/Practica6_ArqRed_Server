from random import *

def ruido(msj):
    newm=list(msj)
    for i in range (len(newm)):
        n=randint(0, 100)
        if n==1:
            newm[i]='-'
    return "".join(newm)

'''
a = ruido('HolaHolaHolaHola'*100)
print(a)
'''


        

            
print(ruido('HolaHolaHolaHola'))