from db_create import dishes, engine
from parse_file import parse
from sqlalchemy import insert
from sqlalchemy import select


def fill_database(link):

    try:
        restaurantName, productsData = parse(link)
    except TypeError:
        print("No restaurant by link")
        return

    for i in productsData:
        exists = select(dishes)\
            .where(dishes.c.name == productsData[i]['name'])\
            .where(dishes.c.price == productsData[i]['price'])\
            .where(dishes.c.restaurant == restaurantName)

        with engine.connect() as conn:
            exists = bool(conn.execute(exists).first())

        if not exists:
            stmt = insert(dishes).values(name=productsData[i]['name'],
                                         price=productsData[i]['price'],
                                         restaurant=restaurantName)

            with engine.connect() as conn:
                conn.execute(stmt)