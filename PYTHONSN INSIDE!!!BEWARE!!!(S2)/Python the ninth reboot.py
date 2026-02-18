# Python The Ninth Reboot:The Infinite Subway
users_name = input("Please enter your name:")
address = input("Please enter your address:")
telephone_number = input("Please enter your telephone number:")
print('''Size: 6-Inch (£1.65) or 12-Inch (£2.05)

Bread Type:
Plain (£0.40),
Wheat (£0.65),
Italian (£0.75),
Cheese & Herbs (£0.80)

Fillings:
Cheese & Tomato (£0.95)
Italian Bacon & Peperoni (£1.10)
Tuna & Mayo (£0.95)
Turkey & Ham (£1.35)
Chicken Teriyaki (£1.40)
Steak & Cheese (£1.95)

Desirable Additions:
Add an additional 5% fee if the customer is eating in the restaurant, as opposed to taking it away''')
bread_type_list = ["plain","wheat","italian","cheese & herbs"]
bread_type = "null"
size_list = ["6-inch","12-inch"]
size = "null"
filling_list = ["cheese & tomato","italian bacon & peperoni","tuna & mayo","turkey & ham","chicken teriyaki","steak & cheese"]
filling = "null"
while bread_type.lower not in bread_type_list:
    bread_type = input("Please enter your bread type:")
while size.lower not in size_list:
    size = input("Please enter your size:")
while filling.lower not in filling_list:
    filling = input("Please enter your filling:")
print(f"Order summary:\nBread type:{bread_type}\nSize:{size}\nFilling:{filling}")




