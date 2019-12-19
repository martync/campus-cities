from peewee import *
from settings import DB_NAME

import sys


IS_RUNNING_TEST = "pytest" in "".join(sys.argv)


# for eq in dir(sys):
#     print(eq, " >>> ", getattr(sys, eq))


db_name = DB_NAME
if IS_RUNNING_TEST:
    db_name = "test_{}".format(db_name)

print(db_name)
db = SqliteDatabase(db_name)
