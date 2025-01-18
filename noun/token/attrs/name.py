from noun.token.name_list import NAME, NONE
from Definitions import (
    elem,
    elem_is_type,
    validated_elem_list
)

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
            name or NONE.NONE,
            elem(self, '_name_type') or NAME,
            invalid_type = NONE.INVALID
        )

    def init_name(self, name: NAME | list[NAME]) -> None:
        if not elem_is_type(self.name, NONE): return
        self._name = name