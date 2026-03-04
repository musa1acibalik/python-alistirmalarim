def selamla(fn):
    def inner():
        print("hoş geldiniz")
        fn()
        print("görüşmek üzere")

    return inner    

@selamla
def gunaydin():
    print("günaydın")

@selamla
def iyigunler():
    print("iyi gunler")     


# g=selamla(günaydın)
# i=selamla(iyigunler)    

gunaydin()
iyigunler()   
    