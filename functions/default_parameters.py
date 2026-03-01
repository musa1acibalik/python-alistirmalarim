# Fonksiyonlarda varsayılan parametreler kullanımı
def selamla(isim="kullanıcı", mesaj="iyi günler"):
    """
    Varsayılan parametreler:
    - isim: kullanıcı
    - mesaj: iyi günler
    """
    return f"{isim} {mesaj}"

# Farklı çağrı örnekleri
sonuc1 = selamla()                 # varsayılan isim ve mesaj
sonuc2 = selamla("Ali")            # sadece isim değiştirdik
sonuc3 = selamla("", "Merhaba")    # isim boş, mesaj değişti

print(sonuc1, sonuc2, sonuc3)