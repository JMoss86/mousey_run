from noun.token.dunders.element import Element
from noun.token.attrs.name import Name
from noun.token.attrs.stattus import Stattus
from noun.token.name_list import NAME, INACTIVE
from Definitions import (
    elem,
    elem_string,
    name_elem_is_type
)

class Token(Element, Name, Stattus):
    __rank = 0

    def __init__(self, name: NAME | list[NAME] | None = None) -> None:
        super().__init__(name = name)
        Token.__rank += 1

    def __str__(self) -> str:
        return super().__str__() + elem_string(self.stattus)

    def activate(self) -> bool:
        if name_elem_is_type(self, INACTIVE): return False
        print(f'\n{self.name} has activated.')
        for stattus in self.stattus:
            if (handle_stattus := elem(self, f'_handle_{stattus}')): handle_stattus()
        return True