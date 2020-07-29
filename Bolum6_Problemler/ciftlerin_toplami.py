from functools import reduce
def toplama(x,y):
    return x+y

liste = [1,2,3,4,5,6,7,8,9,10]
cift_sayilar = list(filter( lambda x : x % 2 == 0,liste))
print(cift_sayilar)
print(reduce(toplama,cift_sayilar))
