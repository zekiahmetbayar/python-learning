
for i in range(1,11):
    print("*************** {} 'lerin tablosu ***************".format(i))
    for j in range(0,11):
        carpim = i*j
        print(" {} x {} = {} ".format(i,j,carpim))
        carpim = 0
        if(j == 10):
            break