def sayi_uret():
    sayi=0
    while True:
        yield sayi ** 2
        sayi +=1

generator=sayi_uret()

print(next(generator))

for i in generator:
    pass# print(i)