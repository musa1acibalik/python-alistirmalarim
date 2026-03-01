# --- Telefon rehberi uygulaması ---

rehber = {}

for i in range(3):
    isim = input("İsim gir: ")
    numara = input("Numara gir: ")
    rehber[isim] = numara

arama = input("Aranacak kişi: ")

if arama in rehber:
    print("Numara:", rehber[arama])
else:
    print("Kişi bulunamadı")


# --- Kelime sayacı ---

cumle = input("\nBir cümle giriniz: ")
kelimeler = cumle.split()

sayac = {}

for kelime in kelimeler:
    if kelime in sayac:
        sayac[kelime] += 1
    else:
        sayac[kelime] = 1

print("Kelime sayıları:")
for kelime, adet in sayac.items():
    print(kelime, ":", adet)


# --- Takipçi karşılaştırma (set kullanımı) ---

takip_ettiklerim = ["Ali", "Ayşe", "Mehmet", "Zeynep"]
beni_takip_edenler = ["Ayşe", "Zeynep"]

set1 = set(takip_ettiklerim)
set2 = set(beni_takip_edenler)

takip_etmeyenler = set1 - set2
ortaklar = set1 & set2

print("\nBeni takip etmeyenler:", takip_etmeyenler)
print("Ortak olanlar:", ortaklar)


# --- Stok yönetim mini programı ---

urunler = {
    "elma": 10,
    "muz": 5,
    "süt": 8
}

while True:

    print("\n1- Ürün ekle / stok artır")
    print("2- Stokları göster")
    print("3- Ürün sil")
    print("4- Çıkış")

    secim = input("Seçim: ")

    if secim == "1":
        urun = input("Ürün adı: ")
        adet = int(input("Kaç adet eklenecek: "))

        if urun in urunler:
            urunler[urun] += adet
        else:
            urunler[urun] = adet

    elif secim == "2":
        for urun, adet in urunler.items():
            print(urun, ":", adet)

    elif secim == "3":
        urun = input("Silinecek ürün: ")
        urunler.pop(urun, None)

    elif secim == "4":
        break

    else:
        print("Geçersiz seçim")
