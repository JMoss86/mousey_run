from noun.token.token import Token
from noun.attrs.place import Place
from noun.attrs.inventory import Inventory

class Noun(Token, Place, Inventory):
    def __init__(self, name = None):
        super().__init__(name = name)
        self.__rank = getattr(self, '_Token__rank')

    @property
    def _rank(self) -> int:
        return self.__rank

    def _update_inventory_place(self) -> None:
        for item in self._inventory:
            # getattr(item, 'set_place')(self.place)
            setattr(item, '_place', self.place)

    def set_place(self, place: 'Noun') -> bool:
        if not super().set_place(place): return False
        place.add_inventory(self)
        self._update_inventory_place()
        return True

    def add_inventory(self, inventory: 'Noun') -> None:
        super().add_inventory(inventory)
        self._update_inventory_place()

    def activate(self) -> bool:
        if not super().activate(): return False
        for item in self._inventory:
            item.activate()
        return True