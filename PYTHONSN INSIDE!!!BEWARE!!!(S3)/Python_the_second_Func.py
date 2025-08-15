import time
import random
def waiting_dots(amount_of_dots = 3,waiting_time = 1):
    for i in range(amount_of_dots):
        print(".")
        time.sleep(waiting_time)
def Processing(Processing="Processing",amount_of_dots = 3,waiting_time = 1):
    print(Processing,end="")
    for i in range(amount_of_dots):
        print(".",end="")
        time.sleep(waiting_time)
# Simple Bar Simulation

menu = {
    "Unbound Beer": 5.0,
    "Wealthed Wine": 7.0,
    "Vastful Whiskey": 10.0,
    "Super-stacked Soda": 2.5,
    "Water": 1.0
}

def show_menu():
    print("Welcome to the Loop Bar!")
    print("Menu:")
    for idx, (item, price) in enumerate(menu.items(), 1):
        print(f"{idx}. {item} - ${price:.2f}")

def take_order():
    order = {}
    while True:
        show_menu()
        choice = input("Enter the number of the item to order (or 'q' to finish): ")
        if choice.lower() == 'q':
            break
        try:
            idx = int(choice) - 1
            if idx < 0 or idx >= len(menu):
                print("Invalid choice. Try again.")
                continue
            item = list(menu.keys())[idx]
            qty = int(input(f"How many {item}s would you like? "))
            if qty <= 0:
                print("Please enter a positive number.")
                continue
            order[item] = order.get(item, 0) + qty
        except ValueError:
            print("Invalid input. Try again.")
    return order

def print_bill(order):
    print("\nYour Order:")
    total = 0
    for item, qty in order.items():
        price = menu[item] * qty
        print(f"{item} x{qty} - ${price:.2f}")
        total += price
    print(f"Total: ${total:.2f}")

def The_Bar():
    order = take_order()
    if order:
        print_bill(order)
    else:
        print("No items ordered. Goodbye!")
    return order

if __name__ == "__main__":
    The_Bar()