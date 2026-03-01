
def not_hesapla():
    satir=satir[:-1]
    list=satir.split(":")

    ogrenciAdi=list[0]
    notlar=list[1].split(",")

    not1=int(notlar[0])
    not2=int(notlar[1])
    not3=int(notlar[2])
    


def not_gir():
    ad=input("ogrenciAdi:")
    soyad=input("ogrSoyad")
    not1=input("not1: ")
    not2=input("not2: ")
    not3=input("not3: ")

    with open("sinav_notlari.txt","+a",encoding="utf-8") as file:
        file.write(ad+' '+soyad+':'+not1+','+not2+','+not3+'\n')



def notlari_oku():
    with open("sinav_notlari.txt","r",encoding="utf") as file:
        for satir in file:
            print(not_hesapla(satir))

def kayit_et():
    pass

while True:
    islem=input("1-Not gir\n2-Notları oku\n3-Notları kayıt et\n4-Çıkış")

    if islem == "1":
        not_gir()


    elif islem=="2":
        notlari_oku()

    elif islem =="3":
        kayit_et()

    elif islem=="4":
        break
    else:
        print("yanliş işlem yaptınız")    

         



