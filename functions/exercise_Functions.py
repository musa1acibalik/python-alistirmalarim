# exercise_Function.py

# -------------------------------
# 1️⃣ Belirli sayıda kelime yazdırma fonksiyonu
# -------------------------------
def yaz(sayi, kelime):
    """
    Girilen sayi kadar kelimeyi ekrana yazdırır.
    """
    for i in range(sayi):
        print(kelime)

# Örnek kullanım
yaz(3, "Python")  # Python kelimesi 3 kez yazdırılır


# -------------------------------
# 2️⃣ Kare alan ve çevre hesaplama fonksiyonları
# -------------------------------
def alan(kenar):
    """
    Kare alanını hesaplar ve döndürür.
    """
    return kenar * kenar

def cevre(kenar):
    """
    Kare çevresini hesaplar ve döndürür.
    """
    return kenar * 4

# Örnek kullanım
print("Alan:", alan(4))   # 16
print("Çevre:", cevre(4)) # 16


# -------------------------------
# 3️⃣ Yazı-tura oyunu fonksiyonu
# -------------------------------
import random

def yaziTura():
    """
    Rastgele 'yazi' veya 'tura' döndürür.
    """
    sayi = random.random()
    if sayi < 0.5:
        return "tura"
    else:
        return "yazi"

# Örnek kullanım
sonuc = yaziTura()
print("Yazı-Tura sonucu:", sonuc)


# -------------------------------
# 4️⃣ Belirli aralıktaki asal sayıları bulma fonksiyonu
# -------------------------------
def asalbul(sayi1, sayi2):
    """
    sayi1 ile sayi2 arasındaki tüm asal sayıları ekrana yazdırır.
    """
    for sayi in range(sayi1, sayi2 + 1):
        if sayi > 1:
            for i in range(2, sayi):
                if sayi % i == 0:
                    break
            else:
                print(f"Asal sayı: {sayi}")

# Örnek kullanım
asalbul(10, 20)


# -------------------------------
# 5️⃣ Bir sayının tam bölenlerini bulma fonksiyonu
# -------------------------------
def tambolenler(sayi):
    """
    Girilen sayının 1 ve kendisi dışında tüm bölenlerini liste olarak döndürür.
    """
    bolenler = []
    for i in range(2, sayi):
        if sayi % i == 0:
            bolenler.append(i)
    return bolenler

# Örnek kullanım
print("20'nin tam bölenleri:", tambolenler(20))