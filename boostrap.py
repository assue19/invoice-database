from models.user import User
from models.invoice import Invoice
from peewee import SqliteDatabase, IntegrityError

DATABASE = SqliteDatabase("invoice.db")


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Invoice], safe=True)
    try:
        User.create(
            first_name="assumpter",
            last_name="Kimeu",
            email="assue@gmail.com",
            company="Acme Corp."
        )
    except IntegrityError:
        pass
    try:
        Invoice.create(
                user_email="assue@gmail.com",
                design_fee=500,
                hosting_fee=175,
                domain_fee=10,
                developer_fee=1000
        )
    except IntegrityError:
        pass
    DATABASE.close()