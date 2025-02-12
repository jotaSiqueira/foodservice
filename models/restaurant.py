from models.menu.menu_iten import MenuIten

class Restaurant:

    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._status = False
        self._ratings = []
        self._menu = []
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f'{self._name} / {self._category} / {self._menu}'
    
    
    @classmethod
    def list_restaurants(cls):
        print(f'{'Restaurant name'.ljust(25)} {'Category'.ljust(25)} {'Rating'.ljust(25)} {'Status'.ljust(25)}')
        for restaurant in cls.restaurants:
            print(f'{restaurant._name.ljust(25)}  {restaurant._category.ljust(25)} {str(restaurant.ratings).ljust(25)}  {restaurant.status.ljust(25)}')

    @property
    def status(self):
        return 'ACTIVE' if self._status else 'INACTIVE'
    
    '''Change the status to active or inactive'''
    def change_status(self):
        self._status = not self._status
    

    def add_menu(self, iten):
        if isinstance(iten, MenuIten):
            self._menu.append(iten)

    def show_menu(self):
        print(f'This is the {self._name} menu')
        for i, iten in enumerate(self._menu, start=1):
            
            if hasattr(iten, 'description'):
                dishe_message = f'{i} Name: {iten._name} | Price: $ {iten._price} | Description:  {iten.description}'
                print(dishe_message)
            else:
                drink_message = f'{i} Name: {iten._name} | Price: $ {iten._price} / Size {iten.size}'
                print(drink_message)