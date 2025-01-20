from noun.token.name_list import STATTUS, INACTIVE
from Definitions import (
    name_elem_is_type,
    add_elem_list,
    sub_elem_list,
    validated_elem_list
)

class Stattus():
    def __init__(self) -> None:
        self._stattus = None
        super().__init__()

    @property
    def _stattus(self) -> list[STATTUS]:
        return self.__stattus

    @property
    def stattus(self) -> list[STATTUS]:
        return self._stattus if not name_elem_is_type(self, INACTIVE) else []

    @_stattus.setter
    def _stattus(self, stattus: STATTUS | list[STATTUS]) -> None:
        if name_elem_is_type(self, INACTIVE): return
        self.__stattus = validated_elem_list(stattus, STATTUS)

    def add_stattus(self, stattus: STATTUS | list[STATTUS]) -> None:
        add_elem_list(self, stattus, '_stattus')

    def sub_stattus(self, stattus: STATTUS | list[STATTUS]) -> None:
        sub_elem_list(self, stattus, '_stattus')