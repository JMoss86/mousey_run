from copy import deepcopy as rtn
from Elem import Element as Elem
from NAME import SBJT, STTS as S

class Sbjt(Elem):
    _NAME = SBJT

    def __init__(self, name: SBJT) -> None:
        self._name = name
        self._stts = []

    def __str__(self) -> str:
        return f'{super().__str__()}{'' if not self.stts else f' {self.stts}'}'

    @property
    def _name(self) -> SBJT:
        return self.__name

    @property
    def _stts(self) -> list[S]:
        return self.__stts

    @property
    def name(self) -> SBJT:
        return rtn(self._name)

    @property
    def stts(self) -> list[S]:
        return rtn(self._stts)

    @_name.setter
    def _name(self, name: SBJT) -> None:
        self.__name = self._vldt_elem(name, self._NAME)

    @_stts.setter
    def _stts(self, stts: list[S]) -> None:
        self.__stts = self._vldt_list(stts, S)

    def _make_list(self, elem: Elem | list[Elem] | None) -> list[Elem]:
        if not elem: return []
        return elem if isinstance(elem, list) else [elem]

    def _cmbn_list(self, this: list[Elem] | None, that: list[Elem] | None) -> list[Elem | None]:
        return [this or [None], that or [None]]

    def _slce_list(self, elst: list[Elem] | None) -> tuple[list[Elem] | None, list[Elem] | None]:
        dflt = [None, None]
        if not elst: return dflt
        return (elst + dflt)[:2]

    def _vldt_list(self, elem: Elem | list[Elem] | None, clss: Elem) -> list[Elem]:
        return self._make_list(self._vldt_elem(elem, clss))

    def _vldt_elem(self, elem: Elem | list[Elem] | None, clss: Elem) -> Elem | list[Elem] | None:
        if not elem: return None
        elif not isinstance(elem, list):
            if not issubclass(type(elem), clss): raise TypeError()
        elif not (all(issubclass(type(e), clss)) for e in elem): raise TypeError()
        return elem

    def _add_elem(self, elem: Elem | list[Elem], attr: str) -> None:
        setattr(self, attr, getattr(self, attr) + self._make_list(elem))

    def _sub_elem(self, elem: Elem | list[Elem], attr: str) -> None:
        setattr(self, attr, [e for e in getattr(self, attr) if e not in self._make_list(elem)])

    def _del_name(self) -> None:
        setattr(self, '_name', None)

    def _add_stts(self, stts: list[S]) -> None:
        self._add_elem(stts, '_stts')

    def _sub_stts(self, stts: list[S]) -> None:
        self._sub_elem(stts, '_stts')

    def add_infc(self) -> None:
        if not self.is_infc(): self._add_stts(S.INFECTED)

    def sub_infc(self) -> None:
        if self.is_infc(): self._sub_stts(S.INFECTED)

    def hndl_infc(self) -> None:
        pass

    def is_infc(self) -> bool:
        return S.INFECTED in self.stts

    def is_agnt(self) -> bool:
        return S.AGENT in self.stts

    def is_frnd(self) -> bool:
        return S.FRIEND in self.stts

    def is_hero(self) -> bool:
        return S.HERO in self.stts

    def is_lock(self) -> bool:
        return S.LOCKED in self.stts

    def is_rebl(self) -> bool:
        return S.REBELLION in self.stts

    def is_burn(self) -> bool:
        return S.BURNING in self.stts

    def is_flud(self) -> bool:
        return S.FLOODED in self.stts