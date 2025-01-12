# from T_Tokn import Tokn as T, TOKN
# from T_Town import Town, rank

# ## Base Token: Want to move to where they Love; won't move if Dead. ##
# class Tokn(T):
#     _TOWN = Town

#     @property
#     def love(self) -> Town:
#         return super().love

#     @property
#     def hate(self) -> Town:
#         return super().hate

#     @property
#     def town(self) -> Town:
#         return super().town

#     def _can_move_to(self, town: Town) -> bool:
#         return self.town != self._vldt(town, self._TOWN) and not town.is_lock()

#     def move(self, town: Town = None) -> None:
#         super().move()
#         if self.is_dead(): return
#         self.hndl_infc()
#         town = town or self.love
#         if not self._can_move_to(town): return
#         self.town.sub_tkns(self)
#         self.set_town(town)
#         self.town.add_tkns(self)

#     def rset(self) -> None:
#         super().move()
#         self.move(self.love)

#     def kill(self) -> None:
#         super().kill()
#         if not self.town: return
#         self.town.sub_tkns(self)
#         self.del_town()
    
# ## Guard Tokens: Sworn to defend the Territories; won't leave a Trek Town unoccupied. Reset to Base. ##
# class Tgrd(Tokn):
#     def __init__(self, name: TOKN, lvht: list[list[Town]] = None):
#         super().__init__(name, lvht)
#         self._base = self.love

#     @property
#     def _base(self) -> Town:
#         return self.__base

#     @property
#     def base(self) -> Town:
#         return self._base

#     @_base.setter
#     def _base(self, base: Town) -> None:
#         self.__base = self._vldt(base, self._TOWN)

#     def set_base(self, base: Town) -> None:
#         self._base = base

#     def _can_move_to(self, town: Town) -> bool:
#         return super()._can_move_to(town) and (not self.town.is_trek() or len(self.town.tkns) > 1)

#     def rset(self) -> None:
#         self.move(self.base)

# ## Traitor Guard Tokens: WiP ##
# class Trtr(Tgrd): # TODO #
#     pass

# ## Special Tokens: Go where they Love, unless an Agent is where they Hate; then they go there. ##
# class Tspc(Tokn):
#     def move(self, town: Town = None) -> None:
#         town = self.hate if not town and any(tokn.is_agnt() for tokn in self.hate.tkns) else town
#         super().move(town)

# ## Kind Tokens: Won't move if Infected, preventing spread. How nice! ##
# class Tknd(Tspc):
#     def move(self, town: Town = None) -> None:
#         if not self.is_infc(): super().move(town)
#         else: self.hndl_infc()

# ## Friend Tokens: Looking to make Friends with an agent, if their Contact is in the same same Town. ##
# class Tfrn(Tknd): # TODO #
#     pass

# ## Mayor Tokens: Award Hero status to Friend if they make it to where they Love, else Foe gets Hero. ##
# class Tmyr(Tknd):
#     def __init__(
#         self,
#         name: TOKN,
#         lvht: list[list[Town]] = None,
#         frfo: list[list[T]] = None
#     ):
#         super().__init__(name, lvht)
#         self._frfo = frfo

#     @property
#     def _frfo(self) -> list[list[T]]:
#         return self.__frfo

#     @property
#     def _frn(self) -> list[T]:
#         return self._frfo[0]

#     @property
#     def _foe(self) -> list[T]:
#         return self._frfo[1]

#     @property
#     def frn(self) -> T:
#         return self._frn[0]

#     @property
#     def foe(self) -> T:
#         return self._foe[0]

#     @_frfo.setter
#     def _frfo(self, frfo: list[list[T]] | None) -> None:
#         frn, foe = self._slce_list(frfo)
#         if (not frn) != (not foe): raise ValueError()
#         self.__frfo = self._cmbn_vldt_list(frn, foe, Tokn)

#     @_frn.setter
#     def _frn(self, frn: list[T]) -> None:
#         self._frfo = [frn, self._foe]

#     @_foe.setter
#     def _foe(self, foe: list[T]) -> None:
#         self._frfo = [self._frn, foe]

#     def _add_frn(self, frn: T) -> None:
#         self._add_elem(frn, '_frn')

#     def _sub_frn(self, love: T) -> None:
#         self._sub_elem(love, '_frn')

#     def _add_foe(self, foe: T) -> None:
#         self._add_elem(foe, '_foe')

#     def _sub_foe(self, foe: T) -> None:
#         self._sub_elem(foe, '_foe')

#     def _at_love(self) -> bool:
#         return self.town == self.love

#     def rset(self) -> None:
#         if not self._at_love() and self.frn: return super().rset()
#         self.frn.add_hero()
#         super().kill()

#     def kill(self) -> None:
#         if not self._at_love() and self.foe: self.foe.add_hero()
#         super().kill()

# ## Spy Tokens: Get killed by Agents; run away when they move from where they Love. ##
# class Tspy(Tspc):
#     def move(self, town: Town = None) -> None:
#         if self.town == self.love: self.kill()
#         super().move(town)
#         if self.town and any(tokn.is_agnt() for tokn in self.town.tkns): self.kill()

#     def rset(self) -> None:
#         self.hndl_infc()

# ## Panacea Token: Completely cures any Infection it encounters, and is then removed. ##
# class Tpna(Tspc):
#     def add_infc(self) -> None:
#         self.sub_infc()
#     def sub_infc(self) -> None:
#         if not self.town: return
#         town = self.town
#         self.kill()
#         town.sub_infc()
#         for tokn in town.tkns:
#             tokn.sub_infc()

# ## Dumb Tokens: Immediately die. ##
# class Tdum(Tokn):
#     def move(self, town: Town = None) -> None:
#         self.kill()
