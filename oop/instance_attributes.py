
#class
class cartitem():
    #constructer => yapıcı metot
    def __init__ (self,name,price,quantity):
        #instance attributes
        self.name=name
        self.price=price
        self.quantity=quantity

    def calculate_total(self):
        return self.price*self.quantity
    
    def applay_discoount(self,rate):
        self.price=self.price * rate
        
            

item1=cartitem("telefon",50000,4)
item2=cartitem("bilgisayar",70000,4)

item1.applay_discoount(0.8)
print(item1.calculate_total())
item2.applay_discoount(0.5)
print(item2.calculate_total())

    