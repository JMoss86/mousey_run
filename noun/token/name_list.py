from noun.token.dunders.element import Element
from enum import auto, Enum

class NAME(Element, Enum):
    pass

class NONE(NAME):
    NONE = auto()

class INACTIVE(NAME):
    RUINED = auto()     ## Place
    USED = auto()       ## Thing
    DEAD = auto()       ## Person

class STATTUS(NAME):
    INFECTED = auto()   ## Person/Place
    BURNING = auto()    ## Person/Place
    AGENT = auto()      ## Person
    FRIEND = auto()     ## Person
    HERO = auto()       ## Person
    LOCKED = auto()     ## Place
    REBELLION = auto()  ## Place
    FLOODED = auto()    ## Place

class NOUN(NAME):
    pass

class PERSON(NOUN):
    PARTY = auto()      ## Agent/Guard
    JEZZEBELLE = auto() ## Agent/Guard :-P
    JUSTIN = auto()     ## Guard :-P
    MOUSETRAP = auto()  ## Guard
    TREVER = auto()     ## Guard
    RABBIT = auto()     ## Token
    CHARLES = auto()    ## Token
    CREEK = auto()      ## Token

class PLACE(NOUN):
    LOCKHAVEN = auto()  ## Trek :-P
    ELMOSS = auto()     ## Trek
    COPPERWOOD = auto() ## Trek
    ROOTWALLOW = auto() ## Trek
    IVYDALE = auto()    ## Town
    BLACKROCK = auto()  ## Town
    WILDERNESS = auto() ## Town :-P

class ITEM(NOUN):
    POISON = auto()
    PANACEA = auto()