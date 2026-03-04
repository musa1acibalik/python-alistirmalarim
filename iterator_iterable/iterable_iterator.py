sayilar=[1,2,3,4,5] #itareble

for i in sayilar:# for  otomatik olarak iterable olan sayılar listesini iteratore çevirir 
    pass #print(i)

#kendimit sayilar listesini iteratore çevirip yazarsak

iterator=iter(sayilar)

while True:
    try:
        sayi=next(iterator)
        print(sayi)

    except StopIteration:
        break        

