

class cartitem():
    #class attributes
    discount_rate=0.8
    item_count=0

    @classmethod
    def display_item_count(cls):
        return f"{cls.item_count} tane ürün oluşturuldu"
    
    @classmethod
    def create_item(cls,data_str):
        name,price,quantity=data_str.split(",")
        return cls(name,price,quantity)


    def __init__ (self,name,price,quantity):
        
        self.name=name
        self.price=price
        self.quantity=quantity
        cartitem.item_count+=1

    def calculate_total(self):
        return self.price*self.quantity
    
    def applay_discoount(self):
        self.price=self.price * cartitem.discount_rate
        
            
print(cartitem.display_item_count())
item1=cartitem("telefon",50000,2)
item2=cartitem("bilgisayar",70000,1)
item3=cartitem("kitap",200,2)
item4=cartitem("kitap",200,2)
print(cartitem.display_item_count())
cartitem.create_item("mouse,800,3")


    