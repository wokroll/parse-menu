from db_create import dishes, engine
from parse_file import parse
from sqlalchemy import insert


def fill_database(link):

    restaurantName, productsData = parse(link)

    for i in productsData:
        stmt = insert(dishes).values(name=productsData[i]['name'],
                                     price=productsData[i]['price'],
                                     restaurant=restaurantName)

        with engine.connect() as conn:
            conn.execute(stmt)