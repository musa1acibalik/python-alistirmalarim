
#class
class cartitem():
    #constructer => yapıcı method
    def __init__ (self,name,price,quantity):
        #instance attributes
        self.name=name
        self.price=price
        self.quantity=quantity

item1=cartitem("telefon",50000,4)
item2=cartitem("bilgisayar",60000,4)

    