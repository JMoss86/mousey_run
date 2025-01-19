from noun.token.token import Token
from noun.token.name_list import INACTIVE
from Definitions import (
    elem,
    name_elem_is_type,
    add_elem_list,
    sub_elem_list,
    validated_elem_list
)

inventory_type = '_inventory_type'

class Inventory():
    def __init__(self) -> None:
        self._inventory = None
        super().__init__()

    @property
    def _inventory(self) -> list[Token]:
        return self.__inventory

    @property
    def inventory(self) -> list[Token]:
        return self._inventory

    @_inventory.setter
    def _inventory(self, inventory: Token | list[Token]) -> None:
        if name_elem_is_type(self, INACTIVE): return
        self.__inventory = validated_elem_list(inventory or [], elem(self, inventory_type) or Token)

    def add_inventory(self, inventory: Token | list[Token]):
        add_elem_list(self, inventory, '_inventory')

    def sub_inventory(self, inventory: Token | list[Token]):
        sub_elem_list(self, inventory, '_inventory')