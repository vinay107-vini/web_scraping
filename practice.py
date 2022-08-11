class shopping_cart:
    products={"iphone":100000,"mac":119000,"ipad":30000}
    quantity={"iphone":5,"mac":3,"ipad":2}

    def __init__(self,wallet):
        self.wallet=wallet
        self.cart={}

    def add_cart(self,name,quan):
        if quan>shopping_cart.quantity[name]:
            raise Exception ("Out of stock")
        else: 
            if name not in self.cart:
                self.cart[name]=quan
                shopping_cart.quantity[name]=shopping_cart.quantity[name]-quan
                self.wallet=self.wallet-shopping_cart.products[name]
            else:
                raise Exception ("Product already in cart")
        

    def remove_items(self,name,quantity):
        if name in self.cart and quantity<=quantity[name]:
            shopping_cart.quantity[name]=shopping_cart.quantity[name]-quantity

customer=shopping_cart(200000)
        