from noun.token.name_list import STATTUS, INACTIVE
from Definitions import (
    name_elem_is_type,
    validated_elem_list,
    add_elem_list,
    sub_elem_list
)

class Stattus():
    def __init__(self):
        self._stattus = None
        super().__init__()

    @property
    def _stattus(self) -> list[STATTUS]:
        return self.__stattus

    @property
    def stattus(self) -> list[STATTUS]:
        return self._stattus

    @_stattus.setter
    def _stattus(self, stattus) -> None:
        if name_elem_is_type(self, INACTIVE): return
        self.__stattus = validated_elem_list(stattus, STATTUS)

    def add_stattus(self, stattus):
        add_elem_list(self, stattus, '_stattus')

    def sub_stattus(self, stattus):
        sub_elem_list(self, stattus, '_stattus')