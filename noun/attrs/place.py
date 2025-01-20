from noun.token.token import Token
from noun.token.name_list import INACTIVE
from Definitions import (
    elem,
    name_elem_is_type,
    set_elem_unless,
    validated_elem_list
)

class Place():
    def __init__(self):
        self._place = None
        super().__init__()

    @property
    def _place(self) -> list[Token]:
        return self.__place

    @property
    def place(self) -> Token:
        return self._place[0]

    @_place.setter
    def _place(self, place: Token | list[Token]) -> None:
        if name_elem_is_type(self, INACTIVE): return
        self.__place = validated_elem_list(
            place,
            elem(self, '_place_type') or Token,
            none_type = None
        )

    def set_place(self, place: Token | list[Token]) -> bool:
        return set_elem_unless(
            self.place == place,
            self,
            place,
            '_place'
        )