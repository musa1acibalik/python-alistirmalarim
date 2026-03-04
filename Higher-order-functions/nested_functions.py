def selamla(isim):
    return f"{isim} merhaba"

print(selamla("memo"))
print(selamla)

merhaba=selamla

print(selamla)
print(merhaba)

del selamla
print(merhaba("memo"))


def outer(number):
    def inner(number):
         print(number)

    inner(number)     


outer(10)

def faktoriyel(sayi):

    if not isinstance(sayi,int):
        raise TypeError("sayı integer olmalı")
    if not sayi>=0:
        raise TypeError("sayı sıfır ya da sıfırdan büyük olmalı")

    def inner_faktoriyel(sayi):
        if sayi<=1:
            return 1
        
        return sayi * inner_faktoriyel(sayi-1)
        
    return inner_faktoriyel(sayi) 

try:
 sonuc=faktoriyel(-5)
 print(sonuc) 

except Exception as ex:
    print(ex)