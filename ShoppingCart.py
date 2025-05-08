

class ShoppingCart:
    """"
    def add_items(self,age,count)
          self.age =age
        self.count = count
        boolI = True

        print(f"{self.age},{self.count},{self.boolI}")

obj1:ShoppingCart =ShoppingCart()
obj2:ShoppingCart =ShoppingCart()
obj2.boolI=False

obj1.add_item(20,1)
obj1.add_item(20,1)
 """


    #This is definition of a list that holds the input content
    def __init__(self):
        self.items=[]

    #The list contains a tuple-the values within are mutable
    #The method add items to the list(as tuples)
    def add_items(self,item_name:str,qty:int,unit_price:float):
      self.items.append((item_name,qty,unit_price))

    #This method looks for the item name in the list and searches from the first item ,once it finds the item,it removes it and we break from the loop
    def remove_item(self,item_name:str):

        for item in self.items:
            if item[0]==item_name:
                self.items.remove(item)
                break

    def calculate_total(self)-> float:
        total=0.0

        for name,qty,price in self.items:
            #loops for the whole tuple to get the total
            total += qty*price
        return total


    def summary(self):

        print("Cart Contents")
        for name,qty,price in self.items:
            print(f"{name}: {qty} @ Ksh {price:.2f} each")

        print(f"Total: Ksh {self.calculate_total():.2f}\n")


# This defines a discount rate
class DiscountedCart(ShoppingCart):
    def __init__(self,discount_rate:float):
        super().__init__()

        self.discount_rate =discount_rate #e.g 0.10 for 10%


    def calculate_total(self) -> float:
        """Override the earlier set method to be able to apply the discounted values"""
        initial_total=super().calculate_total()
        discount = initial_total*self.discount_rate
        return initial_total- discount

class TaxedCart(ShoppingCart):
    def __init__(self,tax_rate: float):
        super().__init__()
        self.tax_rate=tax_rate


    def calculate_total(self) -> float:
        """Override the earlier set method to be able to apply the discounted values"""
        initial_total=super().calculate_total()
        tax = initial_total*self.tax_rate
        return initial_total+tax


def checkout(cart: ShoppingCart):
        cart.summary()
        print(f"Final amount: Ksh{cart.calculate_total():.2f}\n")


#Usage
if __name__== "__main__":
    #Objects-instantiating a class
    cart:ShoppingCart=ShoppingCart()

    cart.add_items("Kiwi",50,79.2)
    cart.add_items("Papaya",30,40.3)
    cart.add_items("Guava",10,20.1)
    cart.add_items("Mango",50,7.6)
    print(">>>>This is the cart without Tax and discount<<<<")
    # print(cart.summary())
    checkout(cart)

    disc_cart = DiscountedCart(discount_rate=0.15)
    disc_cart.add_items("Kiwi", 50, 79.2)
    disc_cart.add_items("Papaya", 30, 40.3)
    disc_cart.add_items("Guava", 10, 20.1)
    disc_cart.add_items("Mango", 50, 7.6)
    print(">>>>The cart with the discounted price applied<<<<")
    checkout(disc_cart)

    taxed_cart = TaxedCart(tax_rate=0.12)
    taxed_cart.add_items("Kiwi", 50, 79.2)
    taxed_cart.add_items("Papaya", 30, 40.3)
    taxed_cart.add_items("Guava", 10, 20.1)
    taxed_cart.add_items("Mango", 50, 7.6)
    print(">>> Applying a 12% Tax  <<<")
    checkout(taxed_cart)

