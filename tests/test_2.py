import unittest
from models import db, Person, Group
from pony.orm import db_session


class Test2(unittest.TestCase):

    @db_session
    def test_2(self):
        person = Person(name='Mary', age=22)
        db.commit()

        group = Group(name='Team 2', people=person)
        db.commit()

        person = group.people.select().get()
        self.assertEqual(person.name, 'Mary')
