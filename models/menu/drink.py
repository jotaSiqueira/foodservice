from models.menu.menu_iten import MenuIten


class Drink(MenuIten):

    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size


    def __str__(self):
        return self._name
    
    def apply_discount(self):
        self._price -= (self._price * 0.05) 