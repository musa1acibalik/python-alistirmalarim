liste=[5, 12, -3, 8, -1, 0, 15]
liste2=[]

for sayi in liste[:]:
    if sayi<0:
        liste.remove(sayi)
    else:
        liste2.append(sayi) 

print(liste)
print(liste2)


