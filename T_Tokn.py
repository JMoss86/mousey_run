from NAME import STTS as S, TOKN
from Sbjt import Sbjt as T, rank

class Tokn(T):
    _NAME = TOKN
    _TOWN = T
    _INFA = 0
    _INFB = 5

    def __init__(self, name: TOKN, lvht: list[list[T]] | None = None) -> None:
        super().__init__(name)
        self._lvht = lvht
        self._town = None
        self._infc = 0

    @property
    def _lvht(self) -> list[list[T]]:
        return self.__lvht

    @property
    def _love(self) -> list[T]:
        return self._lvht[0]

    @property
    def _hate(self) -> list[T]:
        return self._lvht[1]

    @property
    def _town(self) -> T:
        return self.__town

    @property
    def name(self) -> TOKN:
        return super().name

    @property
    def love(self) -> T:
        return self._love[0]

    @property
    def hate(self) -> T:
        return self._hate[0]

    @property
    def town(self) -> T:
        return self._town

    @_lvht.setter
    def _lvht(self, lvht: list[list[T]] | None) -> None:
        love, hate = self._slce_list(lvht)
        if not (love or hate): self.add_agnt()
        elif not (love and hate): raise ValueError()
        self.__lvht = self._cmbn_vldt_list(love, hate, self._TOWN)

    @_love.setter
    def _love(self, love: list[T]) -> None:
        self._lvht = [love, self._hate]

    @_hate.setter
    def _hate(self, hate: list[T]) -> None:
        self._lvht = [self._love, hate]

    @_town.setter
    def _town(self, town: T) -> None:
        self.__town = self._vldt(town, self._TOWN)

    def _add_love(self, love: T) -> None:
        self._add_elem(love, '_love')

    def _add_hate(self, hate: T) -> None:
        self._add_elem(hate, '_hate')

    def _sub_love(self, love: T) -> None:
        self._sub_elem(love, '_love')

    def _sub_hate(self, hate: T) -> None:
        self._sub_elem(hate, '_hate')

    def set_town(self, town: T) -> None:
        setattr(self, '_town', self._vldt(town, self._TOWN))

    def del_town(self) -> None:
        if self.town: setattr(self, '_town', None)

    def add_infc(self) -> None:
        super().add_infc()
        self._infc += 1
        if self.town and not self.town.is_infc(): self._town.add_infc()

    def add_agnt(self) -> None:
        if not self.is_agnt(): self._add_stts(S.AGENT)

    def add_frnd(self) -> None:
        if not self.is_frnd(): self._add_stts(S.FRIEND)

    def add_hero(self) -> None:
        if not self.is_hero(): self._add_stts(S.HERO)

    def sub_infc(self) -> None:
        super().sub_infc()
        self._infc = 0

    def sub_agnt(self) -> None:
        if self.is_agnt(): self._sub_stts(S.AGENT)

    def sub_frnd(self) -> None:
        if self.is_frnd(): self._sub_stts(S.FRIEND)

    def sub_hero(self) -> None:
        if self.is_hero(): self._sub_stts(S.HERO)

    def hndl_infc(self) -> None:
        super().hndl_infc()
        if self._infc > self._INFA: self._infc += 1
        if self._infc > self._INFB: self.kill()

    def is_dead(self) -> bool:
        return not self.town

    def move(self, town: T = None) -> None:
        pass

    def rset(self) -> None:
        pass

    def kill(self) -> None:
        self._del_name()
