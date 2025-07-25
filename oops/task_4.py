'''            TASK 4'''

class Ekart():
    def __init__(self):
        self.cart = []
    def add_prod(self,name,qnt):
        self.cart.append((name,qnt))
        print(f"{qnt} {name} is added to Cart\nCart Items:-")
        for i in self.cart:
            print(f"{i[0]} : {i[1]}")
    def remove_from(self,name):
        found = False
        for i in self.cart:
            if name in i:
               found = True
               self.cart.remove(i)
               print(f"{name} removed")
        if not found:
           print(f"{name} not in the Cart")
    def quantity(self):
        print("\nTotal cart Items :-")
        sum = 0
        for i in self.cart:
            sum += i[1]
            print(f"{i[0]} : {i[1]}")
        print(f"Grand Total: {sum}")

pr = Ekart()
pr.add_prod("iphone",3)
pr.add_prod("Powerbank",2)
pr.remove_from("iphone")
pr.remove_from("Laptop")
pr.quantity()
        