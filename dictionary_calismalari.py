# rehber={}

# for i in range(3):
#     isim=input("isim gir:")
#     numara=input("numara gir:")
#     rehber[isim]=numara

# arama=input("arama yapılcak kişi:")

# if arama in rehber:
#     print("numara:",rehber[arama])
# else:
#     print("kişi bulunamadı")    


# cümle=input("bir cümle giriniz:")
# kelimeler=cümle.split()

# sayaç={}


# for kelime in kelimeler:
#     if kelime in sayaç:
#         sayaç[kelime]+=1
#     else:
#         sayaç[kelime]=1


# for kelime,adet in sayaç.items():
#     print(kelime,"",adet)


# takip_ettiklerim = ["Ali", "Ayşe", "Mehmet", "Zeynep"]
# beni_takip_edenler = ["Ayşe", "Zeynep"]

# set1 = set(takip_ettiklerim)
# set2 = set(beni_takip_edenler)

# takip_etmeyenler = set1 - set2
# ortaklar = set1 & set2

# print("Beni takip etmeyenler:", takip_etmeyenler)
# print("Ortak olanlar:", ortaklar)


# urun=input("ürün adı:")
#         adet=int(input("bu üründen kaç adet var"))
#         urunler[urun]=adet


urunler = {
    "elma": 10,
    "muz": 5,
    "süt": 8
}


while True:

    print("ürün eklemek için 1'e basınız")
    print("stok miktarı için 2'ye basınız:")
    print("ürün silmek için 3'e basınız")
    print("çıkış yapmak için 4'ye basınız:")

    secim=input()

    if secim=="1":
        urun=input("ürün adı:")
        adet=int(input("bu üründen kaç adet var"))
        urunler[urun]=adet

        if urun in urunler:
            urunler[urun] += adet
        else:
            urunler[urun]=adet

    elif secim=="2": 
        for urun,adet in urunler.items():
            print(urun,":",adet)

    elif secim=="3":  
        urun=input("silinecek ürün")
        urunler.pop(urun)

    elif secim=="4":
        break
    else:
        print("geçersiz seçim")    
