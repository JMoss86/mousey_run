from noun.token.dunders.element import Element
from noun.token.attrs.name import Name
from noun.token.attrs.stattus import Stattus
from noun.token.name_list import NAME, INACTIVE, NONE
from Definitions import (
    elem,
    elem_list,
    elem_string,
    elem_is_type
)

class Token(Element, Name, Stattus):
    __rank = 0

    def __init__(self, name: NAME | list[NAME] | None = None) -> None:
        super().__init__(name = name)
        Token.__rank += 1

    def __str__(self) -> str:
        return super().__str__() + elem_string(self.stattus)

    def activate(self) -> bool:
        if (name := self.name) is NONE.NONE or elem_is_type(name, INACTIVE): return False
        print(f'\n{name} has activated.')
        for stattus in self.stattus:
            if (handle_stattus := elem(self, f'_handle_{stattus}')): handle_stattus()
        return True

    def deactivate(self) -> bool:
        if elem_is_type((name := self.name), INACTIVE): return False
        setattr(self, '_Name__name', elem_list(elem(self, '_inactive_type') or NONE.NONE))
        print(f'\n{name} has deactivated.')
        return True