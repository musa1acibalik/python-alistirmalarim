# def sum():
#     return 10+20
# sonuc=sum()
# print(sonuc)


# def calculate_age():
#     import datetime
#     return datetime.datetime.now().year-2001
# print(calculate_age())


def clock():
    import datetime
    return datetime.datetime.now().hour

def selamla():
    if(clock()<12):
        return "günaydın"
    else:
        return "merhaba"
    
print(selamla())    
