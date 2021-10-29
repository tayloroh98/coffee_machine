from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
order_continue = True

def report():
    money_machine.report()
    coffee_maker.report()
while order_continue == True:
    order = input("What would you like? (espresso/latte/cappuccino/):")
    drink = menu.find_drink(order)
    if coffee_maker.is_resource_sufficient(drink):
        total = money_machine.process_coins()
        money_machine.make_payment(total)
        continues = ("do you want another one?")
        if continues == 'no':
            order_continue = False
