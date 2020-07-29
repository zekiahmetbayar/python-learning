sys_id = "zeki"
sys_pass = "1234"
sys_try = 3

while True:
    user_id = input("Kullanıcı adı : ")
    user_pass = input("Parola : ")

    if(sys_id != user_id or sys_pass!=user_pass):
        print("Hata !")
        sys_try -= 1
    else:
        print("Başarılı !")
        break
    
    if(sys_try == 0):
        print("Giriş hakkı kalmadı !")
        break