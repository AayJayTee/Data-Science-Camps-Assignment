class Shopping():
        def __init__(self):
                self.itemsdict = {}
        
        def additems(self,item,price):
                self.itemsdict[item] = price

        def removeitems(self,item):
                del self.itemsdict[item]

        def cal(self):
                total=0
                for i in self.itemsdict.values():
                        total+=i
                print("The total comes out to be: ",total)

shoppingcart = Shopping()
shoppingcart.additems('Book',80)
shoppingcart.additems('Food',150)
shoppingcart.cal()
shoppingcart.removeitems('Book')
shoppingcart.cal()
