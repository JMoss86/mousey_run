from noun.noun import Noun
from noun.token.name_list import (
    PLACE,
    ITEM,
    PERSON,
    INACTIVE
)
from noun.token.name_list import NAME
from Definitions import elem_string

class Macro(Noun):
    def __init__(self, name: NAME | list[NAME] | None = None):
        super().__init__(name)

    def __str__(self):
        return super().__str__() + elem_string(self.inventory)

class Micro(Noun):
    def __init__(self, name: NAME | list[NAME] | None = None):
        self._place_type = Place
        super().__init__(name)

class Place(Macro):
    __rank = 0

    def __init__(self, name: PLACE | list[PLACE] | None = None):
        self._name_type = PLACE
        self._inventory_type = Noun
        self._inactive_type = INACTIVE.RUINED
        super().__init__(name = name)
        Place.__rank += 1

    @property
    def place(self) -> 'Place':
        return self

    @Noun._place.setter
    def _place(self, _) -> None:
        self._Place__place = [None]

class Item(Micro):
    __rank = 0

    def __init__(self, name: ITEM | list[ITEM] | None = None):
        self._name_type = ITEM
        self._inactive_type = INACTIVE.USED
        super().__init__(name = name)
        Item.__rank += 1

    @property
    def inventory(self) -> list['Item']:
        return [self]

    @Micro._inventory.setter
    def _inventory(self, _):
        self._Inventory__inventory = []

class Person(Macro, Micro):
    __rank = 0

    def __init__(self, name: PERSON | list[PERSON] | None = None):
        self._name_type = PERSON
        self._inventory_type = Item
        self._inactive_type = INACTIVE.DEAD
        super().__init__(name = name)
        Person.__rank += 1