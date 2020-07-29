def ucgen_mi(demet):
    if (abs(demet[0]+demet[1]) > demet[2] and abs(demet[0]+demet[2]) > demet[1] and abs(demet[1]+demet[2]) > demet[0]):

       print(" {} sayılarıyla bir üçgen oluşturulabilir.".format(demet))
    
    else:
        print(" {} sayılarıyla bir üçgen oluşturulamaz.".format(demet))
    
demet = [(3,4,5),(6,8,10),(3,10,7)]
print(list(filter(ucgen_mi,demet)))
