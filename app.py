import os
from models.menu.drink import Drink
from models.menu.dishes import Dishes

from models.menu.menu_iten import MenuIten
from models.restaurant import Restaurant

restaurants = []

def show_program_name():

    print('''
███████╗░█████╗░░█████╗░██████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗
█████╗░░██║░░██║██║░░██║██║░░██║
██╔══╝░░██║░░██║██║░░██║██║░░██║
██║░░░░░╚█████╔╝╚█████╔╝██████╔╝
╚═╝░░░░░░╚════╝░░╚════╝░╚═════╝░

░██████╗███████╗██████╗░██╗░░░██╗██╗░█████╗░███████╗
██╔════╝██╔════╝██╔══██╗██║░░░██║██║██╔══██╗██╔════╝
╚█████╗░█████╗░░██████╔╝╚██╗░██╔╝██║██║░░╚═╝█████╗░░
░╚═══██╗██╔══╝░░██╔══██╗░╚████╔╝░██║██║░░██╗██╔══╝░░
██████╔╝███████╗██║░░██║░░╚██╔╝░░██║╚█████╔╝███████╗
╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚══════╝\n''')

def show_options():
    print('1 - Register Restaurant')
    print('2 - List Restaurant ')
    print('3 - Change Restaurant status')
    print('4 - Show the Menu by restaurant name')
    print('5 - Exit\n')

    try:

        choose_option = int(input("Choose one of the options "))
        print('You choose the option ', choose_option)

        match choose_option:
            case 1:
               register_new_restaurant()
            case 2:
                list_restaurants()
            case 3:
                change_restaurant_status()
            case 4:
                show_menu_by_restaurant()
            case 5:
                end_app()
            case _:
                invalid_option()
    except:
        invalid_option()

def back_menu():
    print()
    input('Press a key to return to the main menu  ')
    main()

def invalid_option():
    print('Invalid Option')
    back_menu()


def end_app():
    os.system('cls')
    show_subtitle('Ending Program')

def show_subtitle(text):
    os.system('cls')
    line = '*' * (len(text) + 4)
    print(line)
    print(text)
    print(line)
    print()

def register_new_restaurant():

    '''
    Inputs:
        - Restaurant name
        - Category

    Outputs: 
        - Add a new restaurant to the Restaurant list
    '''
    os.system('cls')
    show_subtitle('Registration of new restaurants  ')
    restaurant_name = input('Enter the name of the restaurant you want to register: \n')
    category = input('Enter the restaurant category  \n')
    restaurant_data = {'name': restaurant_name, 'category': category, 'status': False}
    restaurants.append(restaurant_data)
    print(f'Restaurant {restaurant_name} was successfully registered\n')
    back_menu()

def list_restaurants():
    os.system('cls')
    show_subtitle('Listing restaurants')

    print(f'{'Restaurant name'.ljust(22)} | {'Category'.ljust(20)} | Status')

    for restaurant in restaurants:
        restaurant_name = restaurant['name']
        category = restaurant['category']
        status = 'active' if restaurant['status'] else 'inactive'

        print(f' - {restaurant_name.ljust(20)} - {category.ljust(20)} - {status}') 

    back_menu()


'''Function responsible for changing the status to "active" or "inactive""'''
def change_restaurant_status():
    show_subtitle('Changing restaurant status')
    restaurant_name = input('Enter the name of the restaurant you want to change the status of: ')
    restaurant_found = False

    for restaurant in restaurants:
        if restaurant_name == restaurant['name']:
            restaurant_found = True
            restaurant['status'] = not restaurant['status']
            message = f'The restaurant {restaurant_name} was successfully active' if restaurant['status'] else f'The restaurant {restaurant_name} was successfully inactive'
            print(message)
    if not restaurant_found:
        print('Restaurant not found')

    back_menu()

def show_menu_by_restaurant():
    hamburguer = Dishes('Hamburguer', 20, 'best burguer ever')
    hamburguer.apply_discount()
    show_subtitle('Restaurants Menu')

    if not restaurants:
            print('There is no Restaurant in the list')
    else:
        typed_name = input('Please type the restaurant name to see the menu and prices ')

        for restaurant in restaurants:

            if typed_name == restaurant['name']:
                test = Restaurant(typed_name, 'FastFood')
                test.add_menu(hamburguer)
                test.show_menu()
            else:
                print('Restaurant not found by this name')
        
    back_menu()


def main():
    show_program_name()
    show_options()
    pass
if __name__ == '__main__':
    main()