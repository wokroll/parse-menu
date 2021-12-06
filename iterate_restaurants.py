from fill_db import fill_database

possiblePages = ["https://opc.orty.io/?mid=6524",
                 "https://opc.orty.io/?mid=5763",
                 "https://opc.orty.io/?mid=2698",
                 "https://opc.orty.io/?mid=2617"]


# start, finish - whole numbers to brute-force restaurants
def restaurants_loop(start, finish):

    URL = "https://opc.orty.io/?mid="

    for number in range(start, finish+1):
        restaurantLink = "https://opc.orty.io/?mid=" + str(number)
        print(restaurantLink)
        fill_database(restaurantLink)
