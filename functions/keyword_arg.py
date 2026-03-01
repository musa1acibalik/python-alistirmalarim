# keyword_arg.py

# -------------------------------
# 1️⃣ Full name fonksiyonu
# -------------------------------
def full_name(name: str, lastname: str, age: int) -> str:
    """
    Girilen isim, soyisim ve yaş bilgilerini birleştirerek string olarak döndürür.
    """
    return f"Your name is {name} {lastname}, age: {age}"

# Örnek kullanım
sonuc = full_name("Sadık", "Turan", 24)
print(sonuc)


# -------------------------------
# 2️⃣ Liste elemanlarını toplama fonksiyonu
# -------------------------------
def toplam(liste):
    """
    Verilen liste elemanlarının toplamını döndürür.
    """
    sonuc = 0
    for i in liste:
        sonuc += i
    return sonuc

# Örnek kullanım
sayilar = (10, 20, 30, 40)
print("Liste toplamı:", toplam(sayilar))


# -------------------------------
# 3️⃣ *args ile değişken sayıda argüman toplama
# -------------------------------
def toplama(*args):
    """
    Değişken sayıda argüman alır ve toplamını döndürür.
    """
    print("Args:", args)
    print("Args tipi:", type(args))
    sonuc = 0
    for i in args:
        sonuc += i
    return sonuc

# Örnek kullanım
sonuc = toplama(10, 20, 30, 40)
print("Args toplamı:", sonuc)


# -------------------------------
# 4️⃣ *args ile kullanıcı bilgilerini yazdırma
# -------------------------------
def display_user_args(*args):
    """
    Değişken sayıda argümanı tuple olarak yazdırır.
    """
    print("Args:", args)
    print("Args tipi:", type(args))

# Örnek kullanım
display_user_args("Musa", 25, "Istanbul")


# -------------------------------
# 5️⃣ **kwargs ile kullanıcı bilgilerini yazdırma
# -------------------------------
def display_user_kwargs(**kargs):
    """
    Anahtar-değer şeklindeki argümanları dictionary olarak yazdırır.
    """
    print("Kwargs:", kargs)
    print("Kwargs tipi:", type(kargs))

# Örnek kullanım
display_user_kwargs(name="Musa", age=25, city="Istanbul")