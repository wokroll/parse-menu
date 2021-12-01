from fill_db import fill_database

possiblePages = ["https://opc.orty.io/?mid=2698",
                 "https://opc.orty.io/?mid=5763"]

if __name__ == '__main__':
    fill_database(possiblePages[0])
