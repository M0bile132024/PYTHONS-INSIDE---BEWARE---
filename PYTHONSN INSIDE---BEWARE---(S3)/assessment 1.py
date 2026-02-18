# The Pizza Menu
from time import sleep as s

MENU = '''Pizza menu:
Pizzas are made with tomato and fresh mozzarella cheese base. All pizzas consist of 16 slices.

    1. Cheese and Tomato - Italian style six-cheese blend - £7.50
    2. BQQ Chicken - Chargrilled chicken, barbeque sauce, bacons, onions - £7.90
    3. Meat Feast - Ham, Pepperoni
    4. Piri-Piri Chicken - Chilli pepper sauce,chargrilled chicken - £8.80
    5. Hawaii -
    "Mediterranean",
    "The Mexician",
    "The Works",
    "Garlic bread",
    "Chips'''
def process_order(pizza_ordered):
    global discount1
    global discount2
    global NAME
    PIZZA_LIST = ["Cheese and Tomato",
    "BQQ Chicken",
    "Meat Feast",
    "Piri-Piri Chicken",
    "Hawaii",
    "Mediterranean",
    "The Mexician",
    "The Works",
    "Garlic bread",
    "Chips"]

    print(f"{NAME} , your current order:")

    i = 0
    price_list = []
    for x in pizza_ordered:
        print(f"    Order {i}:{PIZZA_LIST[x-1]} | Cost:£{process_bill(x)}")
        price_list.append(process_bill(x))

    print(f"TOTAL:{total_bill(price_list)}")
    if discount1:
        print("Discount acquired:20% off any order over £40")
    elif discount2:
        print("Minumum order is £7:Delivery charge of £1.50 has been added")
def process_bill(order):
    cost_list = [7.50,7.90,8.10,8.80,8.90,9.50,9.70,9.90,6.50,2.50]
    return cost_list[order]
def total_bill(pricey_list):
    global discount1
    global discount2
    if sum(pricey_list) > 40:
        discount1 = True
        return sum(pricey_list) * 0.8
    elif sum(pricey_list) <= 7:
        discount2 = True
        return sum(pricey_list) + 1.5
    else:
        return sum(pricey_list)
discount1 = False
discount2 = False
print("Welcome to Pizza!")
s(2)
# 1.Record personal details
NAME = input("Please enter your full name:")
ADDRESS = input("Please enter your address(eg:17 Redthorn Road):")
TELEPHONE_NUM = str(input("Please enter your telephone number +"))
# 2. Record pizza orders
ORDER_LIST = []
ORDERED = 0
while ORDERED != "Order" or ORDERED != "order" or len(ORDER_LIST) <= 20:
    print(MENU)
    CURR_ORDER = int(input(f"{NAME} , please enter the number of the pizza you want to order, or enter 'Order' to proceed to billing(Note:Maxuim of 20 pizza per bill):"))
    if CURR_ORDER >= 1 and CURR_ORDER <= 10:
        ORDER_LIST.append(CURR_ORDER)
        print("Order recorded successfully!")
        process_order(ORDER_LIST)
    else:
        print("Invalid order ID.Please try again")
if ORDER_LIST == 20:
    print("Maxuim of 20 pizzas per bill reached, please start a new bill after ordering this one")

# 3.Process order(the hard bit)
# Pizza ordered + price
# Total cost
process_order(ORDER_LIST)





