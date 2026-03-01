
#class
class cartitem():
    #class attributes
    discount_rate=0.8
    item_count=0

    #constructer => yapıcı metot
    def __init__ (self,name,price,quantity):
        #instance attributes
        self.name=name
        self.price=price
        self.quantity=quantity
        cartitem.item_count+=1

    def calculate_total(self):
        return self.price*self.quantity
    
    def applay_discoount(self):
        self.price=self.price * cartitem.discount_rate #class attributes ulaşım şekli
        
            

item1=cartitem("telefon",50000,2)
item2=cartitem("bilgisayar",70000,1)
item3=cartitem("kitap",200,2)

print(item1.__dict__)
print(item2.__dict__)
print(item3.__dict__)
print(cartitem.__dict__)
print(cartitem.item_count)


item1.applay_discoount()
print(item1.calculate_total())
item2.applay_discoount()
print(item2.calculate_total())
item3.applay_discoount()
print(item3.calculate_total())

    