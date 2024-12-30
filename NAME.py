from Elem import Element as Elem
from enum import auto, Enum as E

class ELEM(Elem, E): pass

class STTS(ELEM):       ## STATUSES ##
    INFECTED = auto()   ## Token/Town
    AGENT = auto()      ## Token
    FRIEND = auto()     ## Token
    HERO = auto()       ## Token
    LOCKED = auto()     ## Town
    REBELLION = auto()  ## Town
    BURNING = auto()    ## Town
    FLOODED = auto()    ## Town

class SBJT(ELEM): pass

class TOWN(SBJT):       ## TOWNS ##
    LOCKHAVEN = auto()  ## Trek :-P
    ELMOSS = auto()     ## Trek
    COPPERWOOD = auto() ## Trek
    ROOTWALLOW = auto() ## Trek
    IVYDALE = auto()    ## Town
    BLACKROCK = auto()  ## Town
    WILDERNESS = auto() ## Town :-P

class TOKN(SBJT):       ## TOKENS ##
    PARTY = auto()      ## Agent/Guard
    JEZZEBELLE = auto() ## Agent/Guard :-P
    JUSTIN = auto()     ## Guard :-P
    MOUSETRAP = auto()  ## Guard
    TREVER = auto()     ## Guard
    RABBIT = auto()     ## Token
    CHARLES = auto()    ## Token
    CREEK = auto()      ## Token
    PANACEA = auto()    ## Token