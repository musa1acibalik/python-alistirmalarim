# --- Tuple oluşturma ve eleman erişimi ---

koordinat = (10, 20)

print("X:", koordinat[0])
print("Y:", koordinat[1])


# --- Tuple içinde döngü kullanma ---

sayilar = (1, 2, 3, 4, 5)

toplam = 0

for sayi in sayilar:
    toplam += sayi

print("Toplam:", toplam)


# --- Tuple → liste çevirme (değiştirmek için) ---

renkler = ("kırmızı", "mavi", "yeşil")

renkler_liste = list(renkler)
renkler_liste.append("sarı")

print("Güncellenmiş liste:", renkler_liste)
