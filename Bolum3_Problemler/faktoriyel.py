while True:
    print("Çıkmak için q ya basın.")
    sayi = input("Faktoriyelini bulmak istediğiniz sayı : ")
    if(sayi == 'q'):
        break
    faktoriyel = 1
    for i in range(int(sayi),1,-1):
        faktoriyel *= i
    print(faktoriyel)