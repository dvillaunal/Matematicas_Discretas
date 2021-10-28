"""
### En caso de ser necesario ###
# Best practice, use an environment rather than install in the base env
conda create -n my-env
conda activate my-env
# If you want to install from conda-forge
conda config --env --add channels conda-forge
# The actual install command
conda install numpy
import numpy as np
"""

#Juegos de las Cartas

cart0 = [[i for i in range(1,16,2)],
         [i for i in range(17,32,2)],
         [i for i in range(33,48,2)],
         [i for i in range(49,64,2)]]


cart1 = [[2,3,6,7,10,11,14,15],
         [18,19,22,23,26,27,30,31],
         [34,35,38,39,42,43,46,47],
         [50,51,54,55,58,59,62,63]]


cart2 = [[4,5,6,7,12,13,14,15],
         [20,21,22,23,28,29,30,31],
         [36,37,38,39,44,45,46,47],
         [52,53,54,55,60,61,62,63]]


cart3 = [[8,9,10,11,12,13,14,15],
         [24,25,26,27,28,29,30,31],
         [40,41,42,43,44,45,46,47],
         [56,57,58,59,60,61,62,63]]


cart4 = [[16,17,18,19,20,21,22,23],
         [24,25,26,27,28,29,30,31],
         [48,49,50,51,52,53,54,55],
         [56,57,58,59,60,61,62,63]]

cart5 = [[32,33,34,35,36,37,38,39],
         [40,41,42,43,44,45,46,47],
         [48,49,50,51,52,53,54,55],
         [56,57,58,59,60,61,62,63]]

ct = 0
listac = [cart0, cart1,cart2,cart3,cart4,cart5]
listbinstr = list()

for i in range(0,6):
    print("\n",listac[i][0],"\n", listac[i][1], "\n", listac[i][2], "\n", listac[i][3])
    print(f"Ingrese Un: \n(Si = 1 ó NO = 0) \nsi su numero del 1 al 63 esta en la carta [{ct}]\n")
    ct = ct+1
    x = int(input("=> "))
    if x == 1 or x == 0:
        listbinstr.append(x)
    else:
        print("Ingrese solamente Si = 1 ó NO = 0")
        break

#Resultado
if x == 1 or x == 0:
    listbin = [int(i)*(2**t) for i,t in zip(listbinstr, range(0,6))]

    r = 0

    for t in listbin:
        r = r + t

    print(f"\n---------------\nSu carta es: {r}\n---------------")

else:
    print("\n---------Numero dado Incorrecto---------")
