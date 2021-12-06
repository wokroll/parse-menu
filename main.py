from fill_db import fill_database

possiblePages = ["https://opc.orty.io/?mid=6524",
                 "https://opc.orty.io/?mid=5763",
                 "https://opc.orty.io/?mid=2698",
                 "https://opc.orty.io/?mid=2617"]

if __name__ == '__main__':
    for restaurant in possiblePages:
        fill_database(restaurant)
