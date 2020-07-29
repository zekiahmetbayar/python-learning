# hacker rank
def ekok_bul(sayi1,sayi2):
    ekok = 1
    i = 1
    while(sayi1 > 1 and sayi2 > 1):
        if( not(sayi1%i) and not(sayi2%i)):
            ekok = ekok *i
    return ekok


print(" dadf : ", ekok_bul(6,12))
