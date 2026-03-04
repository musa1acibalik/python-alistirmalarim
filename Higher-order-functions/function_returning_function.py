def UsAlma(taban):
    def inner(us):
        return taban ** us

    return inner

#sonuc=UsAlma(2)(4)
fn=UsAlma(2)
sonuc=fn(4)

print(sonuc)


def yetki_sorgula(sayfa):
    def inner(rolu):
        if rolu=="admin":
            return f"{rolu} rolu {sayfa} sayfasına giriş yapabilir"
        else:
            return f"{rolu} rolu {sayfa} sayfasına giriş yapamaz"
        
    return inner

yetki=yetki_sorgula("ürün güncelle")
sonuc=yetki("user")
print(sonuc)

def islem(islem_adi):
    def toplam(*args):
        toplam=0
        for i in args:
            toplam += i
        return toplam    
    def carpim(*args):
        carpim=1
        for i in args:
            carpim *= i
        return carpim

    if islem_adi=="toplama":
        return toplam
    else:
        return carpim
         




toplama=islem("toplama")
carpma=islem("carpma")

sonuc=toplama(10,20)
sonuc=carpma(5,4)
print(sonuc)

