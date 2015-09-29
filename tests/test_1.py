import unittest
from models import db, Person, Group
from pony.orm import db_session


class Test1(unittest.TestCase):

    @db_session
    def test_1(self):
        person = Person(name='John', age=20)
        db.commit()

        group = Group(name='Team 1', people=person)
        db.commit()

        person = group.people.select().get()
        self.assertEqual(person.name, 'John')
