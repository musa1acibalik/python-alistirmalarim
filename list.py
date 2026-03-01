def parcala(ifade):
    tokens=[]
    sayi=""

    for karakter in ifade:
        if karakter.isdigit():
            sayi+=karakter
        else:
            tokens.append(int(sayi))
            tokens.append(karakter)
            sayi=""


    tokens.append(int(sayi))
    return tokens

def hesapla(tokens):

   
    i = 0
    while i < len(tokens):
        if tokens[i] == "*":
            sonuc = tokens[i-1] * tokens[i+1]
            tokens[i-1:i+2] = [sonuc]
            i = 0

        elif tokens[i] == "/":
            sonuc = tokens[i-1] / tokens[i+1]
            tokens[i-1:i+2] = [sonuc]
            i = 0

        else:
            i += 1

    # sonra + ve -
    sonuc = tokens[0]
    i = 1

    while i<len(tokens):
        if tokens[i] == "+":
            sonuc+=tokens[i+1]
        elif tokens[i] == "-":
            sonuc-=tokens[i+1]

        i+=2    
    
    return sonuc
             
while True:
    ifade=input("bir işlem girim")

    if ifade=="q":
        break

    tokens=parcala(ifade)
    print("sonuc",hesapla(tokens))