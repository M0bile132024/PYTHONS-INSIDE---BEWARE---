# Python assessment retest:Football Club Shop
#Imports
from time import sleep as s
#Varibles:
kit_menu_dict = {
"HOME SHIRT":29.00,
"AWAY SHIRT":29.00,
"SHORTS":12.00,
"SOCKS":6.00,
"TRAINING TOP":18.00,
"TRACK JACKET":35.00,
"CLUB SCARF":8.50,
"CAP":10.00
}
kit_list = list(kit_menu_dict.keys())
size_list = [
"XS-XL",
"XS-XL",
"XS-XL",
"XS-XL",
"XS-XL",
"XS-XL",
"One-size",
"One-size"
]

#Subroutines
def customer_record(name,address,telephone):
    return print(f"Name:{name}\nAddress:{address}\nTelephone number:{telephone}\n")
def menu_display(dictionary):
    i = 0
    for items in dictionary:
        print(f"{items}:£{dictionary[items]} (Size:{size_list[i]})")    #Forgot how to get to 2dp
        i += 1
def checkout(listy,total_costy):
    customer_record(NAME,ADDRESS,TELEPHONE)
    i = 0
    for items in listy:
        i += 1
        print(f"Order {i} ", items ," Size ", order_size_index[i-1] ," Price ", kit_menu_dict[items] , sep="|")
    if total_costy > 45.00:
        print("Special discount:20% off any order over £45!")
        total_costy *= 0.8
    if total_costy < 30.00:
        print("Minimum order is £30 pounds;£1.50 delivery charge added.")
        total_costy += 1.50
    if "One-size" in order_size_index:
        print("One size purchasees;incur 10% hike")
        total_costy *= 1.1
    print(f"TOTAL COST:{total_costy}")


#Main code

#Stage one:Customer record
print("Welcome to the Football Club Shop!")
#s(2)
NAME = input("Please enter your name:")
ADDRESS = input("Please enter your address:")
TELEPHONE = input("Please enter your telephone number: +44 ")
print("Processing info...")
#s(2)
#Stage 2:Menu display
print("Menu:")
menu_display(kit_menu_dict)
#s(2)

#Stage 3:Ordering
ordered = []
order_size_index = []
total_cost = 0
kit_count = 0
while kit_count < 5:
    order = input("Please input the kit you wish to purchase(Maximum of five purchases) or type 'done' to proceed to checkout:").upper()
    if order in kit_menu_dict.keys():
        ordered.append(order)
        order_size_index.append(size_list[kit_list.index(order)])

        total_cost += kit_menu_dict[order]
        kit_count += 1
        print("Order successfully recorded!")
    elif order == "DONE":
        break
    else:
        print("Invalid choice,please try again.")
        continue
if kit_count >= 5:
    print("Maximum amount of kit purchased.Please start a new order after checkout.")
print("Processing order...")
#s(2)
print("CHECKOUT:")
checkout(ordered,total_cost)




