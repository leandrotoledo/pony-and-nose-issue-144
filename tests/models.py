from pony.orm import *

db = Database()


class Person(db.Entity):
    name = Required(str)
    age = Required(int)
    group = Set('Group')


class Group(db.Entity):
    name = Required(str)
    people = Set('Person')


db.bind('sqlite', 'db.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
