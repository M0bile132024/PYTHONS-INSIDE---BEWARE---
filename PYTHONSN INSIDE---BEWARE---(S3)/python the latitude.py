# Python the latitiude
while True:
    city_and_latitude = input("Please enter the name of a city in Europe and its latitude(comma(,) in-between each):").lower().strip().split(sep=",")
    if float(city_and_latitude[1]) > 51.5074:
        print(f"{city_and_latitude[0]} is north of London!")
    elif float(city_and_latitude[1]) < 51.5074:
        print(f"{city_and_latitude[0]} is south of London!")
    else:
        print(f"{city_and_latitude[0]} has the same latitude as London!")
