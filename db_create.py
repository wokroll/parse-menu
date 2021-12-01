from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Date, Integer, String
from sqlalchemy import MetaData

dbLink = "restaurants.db"
metadata_obj = MetaData()
engine = create_engine("sqlite+pysqlite:///"+dbLink, echo=True)

dishes = Table(
    "dishes",
    metadata_obj,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(50)),
    Column('price', String(10)),
    Column('restaurant', String(50))
)

metadata_obj.create_all(engine)

# Session = sessionmaker(bind = engine)
# session = Session()
