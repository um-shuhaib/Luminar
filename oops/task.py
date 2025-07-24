
# qn - 2


# Ekart - add_product(name,quantity)
# cart =[(),()]
# remove from cart
# total quantity


# class Ekart():
#     def __init__(self,name,quantity):
#         self.cart=[]
#         self.cart.append((name,quantity))
#     def add_product(self,name , Quantity):
#         # self.cart.append((name,Quantity))
#         print(f"Your Cart!\nItem Name: {self.cart[0][0]}\nQuantity: {self.cart[0][1]}")             # modify it - after
#     def remove_from(self,name):
#         if self.cart[0][0] != name:
#             print(f"{name} is not in the list")
#         else: 
            
#             self.cart[0] = (self.cart[0][0],self.cart[0][1]-1)
            
#             print(self.cart)
#     def count(self):
#         print(f"Total count: {self.cart[0][1]}")



# pro1 = Ekart("onion",12)
# pro1.add_product()
# # pro1.add_product("banana",4)
# pro1.remove_from("onion")
# pro1.count()


class Ekart():
    def __init__(self,name,qnt):
        self.cart = []
        self.cart.append((name,qnt))
    def add_prod(self,name,qnt):
        self.cart.append((name,qnt))
        for i,item in self.cart:
            
        