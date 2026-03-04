def filter(fn,liste):
    result=[]
    for i in liste:
        if fn(i):
            result.append(i)

    return result

def is_even(num):
    return num % 2==0
def is_positive(num):
    return num >0 

sayilar=[1,2,-3,6,7,-9]

sonuc=filter(is_even,sayilar)
sonuc=filter(is_positive,sayilar)
print(sonuc)