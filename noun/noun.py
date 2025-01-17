from noun.token.token import Token
from noun.attrs.place import Place
from noun.attrs.inventory import Inventory
from Definitions import update_inventory_place

class Noun(Token, Place, Inventory):
    def __init__(self, name = None):
        super().__init__(name = name)
        self.__rank = getattr(self, '_Token__rank')

    @property
    def _rank(self) -> int:
        return self.__rank

    def set_place(self, place: 'Noun') -> bool:
        if not super().set_place(place): return False
        place.add_inventory(self)
        update_inventory_place(self)
        return True

    def add_inventory(self, inventory: 'Noun') -> None:
        super().add_inventory(inventory)
        update_inventory_place(self)

    def activate(self) -> bool:
        if not super().activate(): return False
        for item in self._inventory:
            item.activate()
        return True