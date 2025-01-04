#Pthon The 9th:SUBSWAY
'''Task:Do subway

Eat Fresh Menu
Size:
6-Inch (£1.65) or
12-Inch (£2.05)
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
Add an additional 5% fee if the customer is eating in the restaurant, as opposed to taking it away
# Your dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Convert dictionary keys to a list
keys = list(my_dict.keys())

# Access the first key and its value
first_key = keys[0]
value = my_dict[first_key]

print(f"The first key is '{first_key}' with the value {value}")
'''
import time
def SUBSWAY(sizes,bread_type,fillings,location):
    sizes_dict = {
        "3-inch":1.45,
        "6-inch":1.65,
        "9-inch":1.85,
        "MEGA 12-inch":2.05
    }
    sizes_list = list(sizes_dict.keys())

    bread_type_dict = {
        "Plain":0.40,
        "Wheat":0.65,
        "Oat":0.90,
        "Barley":1.05,
        "Garlic":1.30,
        "Cheese & herbs":1.55,
        "Italian":1.80
    }
    bread_type_list = list(bread_type_dict)
    fillings_dict = {
        "Cheese & Tomato":0.95,
        "Italian Bacon & Peperoni":1.10,
        "Tuna & Mayo":0.95,
        "Turkey & Ham":1.35,
        "Chicken Teriyaki":1.40,
        "Steak & Cheese":1.95,
        "Hunted snake":16.09,
        "Hunted chicken":2.95,
        "Meat-feast":6.99
    }
    fillings_list = list(fillings_dict)
    location_dict = {
        "Restaurant":1.05,
        "Takeway/Premium member!!!":1,
        "Drive-thru":1.025
    }
    location_list = list(location_dict)
    print("|Size", sizes_list[sizes] , "Price" , f"£{sizes_dict[sizes_list[sizes]]}" , "\n","Bread type", bread_type_list[bread_type] , "Price" , f"£{bread_type_dict[bread_type_list[bread_type]]}" , "\n","Fillings", fillings_list[fillings] , "Price" , f"£{fillings_dict[fillings_list[fillings]]}" , "\n" , "Location", location_list[location] , "Percentage change" , f"{(location_dict[location_list[location]]-1)*100:.1f}%" , "\n", "Total cost" , f"£{((sizes_dict[sizes_list[sizes]]+bread_type_dict[bread_type_list[bread_type]]+fillings_dict[fillings_list[fillings]])*location_dict[location_list[location]]):.2f}",sep="|")
print("Welcome to the Python the 9th Subway, the most unsuspicious subway across the Pythonic East!!!!")
time.sleep(4)
print("With hundreds of the most unique toppings to put on that bread bun, here at PT9 Subway, we do that, with 200% the love.....")
time.sleep(4)
print("*sniffs*Feeling hungry?Then smash that enter key, for were going to make you...")
time.sleep(4)
print("THE")
time.sleep(1)
print("BEST")
time.sleep(1)
print("SUB")
time.sleep(1)
print("KNOWN")
time.sleep(1)
print("TO")
time.sleep(1)
print("SNAKE")
time.sleep(3)
input("getit?for we're snakes and you-you know what,nevermind just hit enter...")
print("GREAT!Let's get started!")
quitting = 0
while quitting == 0:
    print("""Let's start with i n c h e s-and I mean, I N C H E S; size always matters around these parts
          |
          |
          |
          v
          Type 0 for our 3 inch sandwich(£1.45),
          1 for our 6(1.65)
          2 is 9(£1.85)
          and 3 is for the MEGA 12-inch(£2.05)""")
    size = int(input(""))
    
    
    
        
    
