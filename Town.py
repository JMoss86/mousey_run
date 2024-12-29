from Template_Tokn import Tokn, rnk
from Template_Town import Town as T

## Base Town; spreads infection to all Tokens. ##
class Town(T):
    _TOKN = Tokn

    @property
    def tkns(self) -> list[Tokn]:
        return super().tkns

    @T._tkns.setter
    def _tkns(self, tkns: list[Tokn]) -> None:
        T._tkns.fset(self, tkns)
        self.__tkns.sort(key = lambda t: rnk(t))
        if self.is_infc() or any(tokn.is_infc() for tokn in self.tkns): self.add_infc()
        for tokn in self.tkns:
            tokn.set_town(self)

## Outside of Lockhaven's influence; become locked if empty. ##
class Trek(Town):
    @Town._tkns.setter
    def _tkns(self, tkns: list[Tokn]) -> None:
        Town._tkns.fset(self, tkns)
        if len(self.tkns) < 1 and not self.is_lock(): self.add_lock()
        elif len(self.tkns) > 0 and self.is_lock(): self.sub_lock()

    def is_trek(self) -> bool:
        return True