hesap = [
    {
        "ad": "musa acıbalık",
        "hesapNo": "123456",
        "bakiye": 25400,
        "ekHesap": 12000,
        "userName": "musaacibalik",
        "pasword": "1234"
    },
    {
        "ad": "mehmet acıbalık",
        "hesapNo": "654321",
        "bakiye": 25400,
        "ekHesap": 12000,
        "userName": "mehmetacibalik",
        "pasword": "4321"
    }
]


def menu(hesap):

    while True:
        print(f"\nMerhaba {hesap['ad']}")
        print("1- Bakiye Sorgulama")
        print("2- Para Çekme")
        print("3- Para Yatırma")
        print("4- Çıkış")

        islem = input("Seçiniz: ")

        if islem == "1":
            bakiyeSorgula(hesap)

        elif islem == "2":
            paracekme(hesap)

        elif islem == "3":
            parayatirma(hesap)

        elif islem == "4":
            print("Çıkış yapıldı")
            break

        else:
            print("Yanlış giriş!")


def bakiyeSorgula(hesap):
    print(f"Bakiye: {hesap['bakiye']}")
    print(f"Ek hesap: {hesap['ekHesap']}")


def paracekme(hesap):

    miktar = float(input("Çekmek istediğiniz miktar: "))

    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] -= miktar
        print("Paranızı alabilirsiniz")

    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]

        if toplam >= miktar:
            izin = input("Ek hesap kullanılsın mı? (e/h): ")

            if izin == "e":
                kalan = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= kalan
                print("Paranızı alabilirsiniz")

            else:
                print("Bakiye yetersiz")

        else:
            print("Bakiye yetersiz")


def parayatirma(hesap):

    miktar = float(input("Yatırılacak miktar: "))
    hesap["bakiye"] += miktar
    print("Para yatırıldı")


def login():

    username = input("Username: ")
    password = input("Password: ")

    for kullanici in hesap:
        if kullanici["userName"] == username and kullanici["pasword"] == password:
            menu(kullanici)
            return

    print("Hatalı giriş!")


login()