from NAME import STTS as S, TOWN
from Sbjt import Sbjt as T, rank

class Town(T):
    _NAME = TOWN
    _TOKN = T

    def __init__(self, name: TOWN, tkns: list[T] | None = None) -> None:
        super().__init__(name)
        self._tkns = tkns

    def __str__(self) -> str:
        return f'{super().__str__()}{'' if not self.tkns else f':\n{self.tkns}'}'

    @property
    def _tkns(self) -> list[T]:
        return self.__tkns

    @property
    def name(self) -> TOWN:
        return super().name

    @property
    def tkns(self) -> list[T]:
        return self._tkns

    @_tkns.setter
    def _tkns(self, tkns: list[T]) -> None:
        self.__tkns = self._vldt_list(tkns, self._TOKN)

    def add_tkns(self, tkns: list[T]) -> None:
        self._add_elem(tkns, '_tkns')

    def sub_tkns(self, tkns: list[T]) -> None:
        self._sub_elem(tkns, '_tkns')

    def add_infc(self) -> None:
        super().add_infc()
        for tokn in self.tkns:
            tokn.add_infc()

    def add_lock(self) -> None:
        if not self.is_lock(): self._add_stts(S.LOCKED)

    def add_rebl(self) -> None:
        if not self.is_rebl(): self._add_stts(S.REBELLION)

    def add_burn(self) -> None:
        if not self.is_burn(): self._add_stts(S.BURNING)

    def add_flud(self) -> None:
        if not self.is_flud(): self._add_stts(S.FLOODED)

    def sub_lock(self) -> None:
        if self.is_lock(): self._sub_stts(S.LOCKED)

    def sub_rebl(self) -> None:
        if self.is_rebl(): self._sub_stts(S.REBELLION)

    def sub_burn(self) -> None:
        if self.is_burn(): self._sub_stts(S.BURNING)

    def sub_flud(self) -> None:
        if self.is_flud(): self._sub_stts(S.FLOODED)

    def is_trek(self) -> bool:
        return False
