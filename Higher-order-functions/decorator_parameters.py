def double(fn):
    def inner(*args,**keyw):
        fn(*args,**keyw)
        fn(*args,**keyw)

    return inner    

@double
def merhaba():
    print("merhaba")

def selam(isim):
    print("selam",isim)  

merhaba()
selam("musa")      