# passing_Parameters.py

# -------------------------------
# 1️⃣ Selamlaşma fonksiyonu (isim parametresi ile)
# -------------------------------
def selamla(isim):
    """
    Girilen isme göre selamlaşma mesajı döndürür.
    """
    return "Merhaba " + isim

# Örnek kullanım
print(selamla("Sadık"))


# -------------------------------
# 2️⃣ Basit toplama fonksiyonu
# -------------------------------
def hesapla(say1, say2):
    """
    İki sayıyı toplar ve sonucu döndürür.
    """
    return say1 + say2

# Örnek kullanım
print("Toplama sonucu:", hesapla(10, 20))


# -------------------------------
# 3️⃣ Yaş ve emeklilik hesaplama fonksiyonları
# -------------------------------
def yashesapla(dogumyili):
    """
    Verilen doğum yılına göre yaş hesaplar.
    """
    return 2026 - dogumyili

def emekliligeKacYilKaldi(dogumyili, isim):
    """
    Emekliliğe kaç yıl kaldığını hesaplar.
    Eğer kişi zaten emekli olmuşsa bunu belirtir.
    """
    yas = yashesapla(dogumyili)
    kalansure = 65 - yas
    if kalansure > 0:
        return f"{isim}, emekliliğinize {kalansure} yıl kaldı"
    else:
        return f"{isim}, zaten {abs(kalansure)} yıl önce emekli oldun"

# Örnek kullanım
print(emekliligeKacYilKaldi(2001, "Musa"))