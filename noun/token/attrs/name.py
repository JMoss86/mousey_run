from noun.token.name_list import NAME, NONE
from Definitions import (
    elem,
    elem_is_type,
    set_elem_unless,
    validated_elem_list
)

none = NONE.NONE

class Name():
    def __init__(self, name: NAME | list[NAME] | None = None) -> None:
        self._name = name
        super().__init__()

    @property
    def _name(self) -> list[NAME]:
        return self.__name

    @property
    def name(self) -> NAME:
        return self._name[0]

    @_name.setter
    def _name(self, name: NAME | list[NAME]) -> None:
        self.__name = validated_elem_list(
            name,
            elem(self, '_name_type') or NAME,
            none_type = none
        )

    def set_name(self, name: NAME | list[NAME]) -> bool:
        return set_elem_unless(
            not elem_is_type(self.name, none),
            self,
            name,
            '_name'
        )