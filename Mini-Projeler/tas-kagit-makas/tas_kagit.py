import random
import sys
import os
import time

count = 0
user_score = 0
computer_score = 0

while True:
    computer_pick = random.randint(0,3)
    if count == 0:
            user_pick = int(input(""" 
                ----------------------------------------

                Taş Kağıt Makas Oynamak İster misin ?

                1 - Taş 

                2 - Kağıt

                3 - Makas

                Seçimini Yap !

                ----------------------------------------
                """))

            # Taş > Makas
            # Makas > Kağıt
            # Kağıt > Taş

            
            computer_pick_names = {1 : 'Taş', 2 : 'Kağıt', 3 : 'Makas'}
            print("Oynanıyor....")
            time.sleep(1)
            if user_pick == 1:
                if computer_pick == 1:
                    print("Senin Seçimin : {} ".format(computer_pick_names[user_pick]))
                    print("Bilgisayarın Seçimi : {} ".format(computer_pick_names[computer_pick]))
                    print("Berabere ! Taş, Taşı yenemez. Tekrar Dene !")
                    print("Skor {} : {} ".format(user_score,computer_score))
                    
                    
                
                elif computer_pick == 2:
                    print("Senin Seçimin : {} ".format(computer_pick_names[user_pick]))
                    print("Bilgisayarın Seçimi : {} ".format(computer_pick_names[computer_pick]))
                    print("Yenildin ! Kağıt Taşı Sarar.")
                    computer_score += 1
                    print("Skor {} : {} ".format(user_score,computer_score))

                elif computer_pick == 3:
                    print("Senin Seçimin : {} ".format(computer_pick_names[user_pick]))
                    print("Bilgisayarın Seçimi : {} ".format(computer_pick_names[computer_pick]))
                    print("Kazandın ! Taş Makası Kırar.")
                    user_score += 1
                    print("Skor {} : {} ".format(user_score,computer_score))

            if user_pick == 2:
                if computer_pick == 1:
                    print("Senin Seçimin : {} ".format(computer_pick_names[user_pick]))
                    print("Bilgisayarın Seçimi : {} ".format(computer_pick_names[computer_pick]))
                    print("Kazandın ! Kağıt Makası Sarar.")
                    user_score += 1
                    print("Skor {} : {} ".format(user_score,computer_score))
                
                elif computer_pick == 2:
                    print("Senin Seçimin : {} ".format(computer_pick_names[user_pick]))
                    print("Bilgisayarın Seçimi : {} ".format(computer_pick_names[computer_pick]))
                    print("Berabere ! Kağıt, Kağıdı Yenemez. Tekrar Dene !")
                    print("Skor {} : {} ".format(user_score,computer_score))

                elif computer_pick == 3:
                    print("Senin Seçimin : {} ".format(computer_pick_names[user_pick]))
                    print("Bilgisayarın Seçimi : {} ".format(computer_pick_names[computer_pick]))
                    print("Yenildin ! Makas Kağıdı Keser.")
                    computer_score += 1
                    print("Skor {} : {} ".format(user_score,computer_score))

            if user_pick == 3:
                if computer_pick == 1:
                    print("Senin Seçimin : {} ".format(computer_pick_names[user_pick]))
                    print("Bilgisayarın Seçimi : {} ".format(computer_pick_names[computer_pick]))
                    print("Yenildin ! Taş Makası Kırar.")
                    computer_score += 1
                    print("Skor {} : {} ".format(user_score,computer_score))
                
                elif computer_pick == 2:
                    print("Senin Seçimin : {} ".format(computer_pick_names[user_pick]))
                    print("Bilgisayarın Seçimi : {} ".format(computer_pick_names[computer_pick]))
                    print("Kazandın ! Makas Kağıdı Keser.")
                    user_score += 1
                    print("Skor {} : {} ".format(user_score,computer_score))

                elif computer_pick == 3:
                    print("Senin Seçimin : {} ".format(computer_pick_names[user_pick]))
                    print("Bilgisayarın Seçimi : {} ".format(computer_pick_names[computer_pick]))
                    print("Berabere ! Makas, Makasa Zarar Veremez. Tekrar Dene !")
                    print("Skor {} : {} ".format(user_score,computer_score))
                
            count += 1
            

    if(count >= 1):
        play_again = input("Tekrar Oynamak İstiyorsan 'Y' istemiyorsan 'N' tuşuna bas !")
        if(play_again == str('Y')):

            user_pick = int(input(""" 
            ----------------------------------------

            Taş Kağıt Makas Oynamak İster misin ?

            1 - Taş 

            2 - Kağıt

            3 - Makas

            Seçimini Yap !

            ----------------------------------------
            """))

            # Taş > Makas
            # Makas > Kağıt
            # Kağıt > Taş

            
            computer_pick_names = {1 : 'Taş', 2 : 'Kağıt', 3 : 'Makas'}
            print("Oynanıyor....")
            time.sleep(1)
            if user_pick == 1:
                if computer_pick == 1:
                    print("Senin Seçimin : {} ".format(computer_pick_names[user_pick]))
                    print("Bilgisayarın Seçimi : {} ".format(computer_pick_names[computer_pick]))
                    print("Berabere ! Taş, Taşı yenemez. Tekrar Dene !")
                    print("Skor {} : {} ".format(user_score,computer_score))
                
                elif computer_pick == 2:
                    print("Senin Seçimin : {} ".format(computer_pick_names[user_pick]))
                    print("Bilgisayarın Seçimi : {} ".format(computer_pick_names[computer_pick]))
                    print("Yenildin ! Kağıt Taşı Sarar.")
                    computer_score += 1
                    print("Skor {} : {} ".format(user_score,computer_score))

                elif computer_pick == 3:
                    print("Senin Seçimin : {} ".format(computer_pick_names[user_pick]))
                    print("Bilgisayarın Seçimi : {} ".format(computer_pick_names[computer_pick]))
                    print("Kazandın ! Taş Makası Kırar.")
                    user_score += 1
                    print("Skor {} : {} ".format(user_score,computer_score))

            if user_pick == 2:
                if computer_pick == 1:
                    print("Senin Seçimin : {} ".format(computer_pick_names[user_pick]))
                    print("Bilgisayarın Seçimi : {} ".format(computer_pick_names[computer_pick]))
                    print("Kazandın ! Kağıt Makası Sarar.")
                    user_score += 1
                    print("Skor {} : {} ".format(user_score,computer_score))
                
                elif computer_pick == 2:
                    print("Senin Seçimin : {} ".format(computer_pick_names[user_pick]))
                    print("Bilgisayarın Seçimi : {} ".format(computer_pick_names[computer_pick]))
                    print("Berabere ! Kağıt, Kağıdı Yenemez. Tekrar Dene !")
                    print("Skor {} : {} ".format(user_score,computer_score))

                elif computer_pick == 3:
                    print("Senin Seçimin : {} ".format(computer_pick_names[user_pick]))
                    print("Bilgisayarın Seçimi : {} ".format(computer_pick_names[computer_pick]))
                    print("Yenildin ! Makas Kağıdı Keser.")
                    computer_score += 1
                    print("Skor {} : {} ".format(user_score,computer_score))

            if user_pick == 3:
                if computer_pick == 1:
                    print("Senin Seçimin : {} ".format(computer_pick_names[user_pick]))
                    print("Bilgisayarın Seçimi : {} ".format(computer_pick_names[computer_pick]))
                    print("Yenildin ! Taş Makası Kırar.")
                    computer_score += 1
                    print("Skor {} : {} ".format(user_score,computer_score))
                
                elif computer_pick == 2:
                    print("Senin Seçimin : {} ".format(computer_pick_names[user_pick]))
                    print("Bilgisayarın Seçimi : {} ".format(computer_pick_names[computer_pick]))
                    print("Kazandın ! Makas Kağıdı Keser.")
                    user_score += 1
                    print("Skor {} : {} ".format(user_score,computer_score))

                elif computer_pick == 3:
                    print("Senin Seçimin : {} ".format(computer_pick_names[user_pick]))
                    print("Bilgisayarın Seçimi : {} ".format(computer_pick_names[computer_pick]))
                    print("Berabere ! Makas, Makasa Zarar Veremez. Tekrar Dene !")
                    print("Skor {} : {} ".format(user_score,computer_score))
        
        if(play_again == str('N')):
            print("Görüşmek üzere ! ")
            break