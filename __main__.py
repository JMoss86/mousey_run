import traceback
from noun.noun import Noun
from noun.types import Person
from noun.types import Place
from noun.types import Item
from noun.token.name_list import (
    STATTUS,
    PLACE,
    ITEM,
    PERSON
)

def main():
    noun = Noun()
    test = Place(ITEM.PANACEA)
    place = Place(PLACE.ELMOSS)
    item = Item(ITEM.PANACEA)
    person = Person(PERSON.PARTY)

    def print_place(): print(f'\n{place}')

    print_place()

    person.set_place(place)

    print_place()

    person.add_inventory(item)

    print_place()

    person.add_stattus(STATTUS.INFECTED)

    print_place()

    place.activate()

    print(f'\n{place == place}')

    print(f'\n{place == Place(PLACE.ELMOSS)}')

    print(f'\n{place == PLACE.ELMOSS}')

    print('\nEND')

if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(traceback.format_exc())

# import traceback
# from NAME import TOKN as TK, TOWN as TN
# from Tokn import Tdum, Tfrn, Tgrd, Tmyr, Tpna, Tspy
# from Town import Trek

# def main():
#     lockh = Trek(TN.LOCKHAVEN)
#     elmos = Trek(TN.ELMOSS)
#     coppr = Trek(TN.COPPERWOOD)
#     rootw = Trek(TN.ROOTWALLOW)

#     elmos.add_infc()

#     stdrd = [coppr, rootw]
#     specl = [rootw, elmos]

#     agnts = [
#         party := Tgrd(TK.PARTY),
#         jezze := Tgrd(TK.JEZZEBELLE)
#     ]
#     tokns = [
#         justn := Tdum(TK.JUSTIN, specl),
#         mtrap := Tgrd(TK.MOUSETRAP, stdrd),
#         trevr := Tgrd(TK.TREVER, specl),
#         charl := Tmyr(TK.CHARLES, stdrd, agnts),
#         rabbt := Tfrn(TK.RABBIT, stdrd),
#         creek := Tspy(TK.CREEK, stdrd[::-1]),
#         panac := Tpna(TK.PANACEA, specl)
#     ]

#     for tgrd in [party, jezze, mtrap, trevr]:
#         tgrd.set_base(lockh)

#     lockh.add_tkns([
#         party,
#         jezze,
#         justn,
#         mtrap,
#         creek,
#         panac
#     ])
#     elmos.add_tkns(charl)
#     coppr.add_tkns(trevr)
#     rootw.add_tkns(rabbt)

#     def dspl() -> None:
#         print(f'~~~~\n{lockh}\n\n{elmos}\n\n{coppr}\n\n{rootw}\n~~~~')
#     def move_tks() -> None:
#         for tokn in tokns:
#             tokn.move()
#             dspl()
#     def rset_all() -> None:
#         for agnt in agnts:
#             agnt.rset()
#             dspl()
#         for tokn in tokns:
#             tokn.rset()
#             dspl()
#     def run_season() -> None:
#         move_tks()
#         rset_all()
#     def jezze_move(trek: Trek) -> None:
#         dspl()
#         jezze.move(trek)
#         dspl()
#         run_season()

#     dspl()
#     print('~~~~ WINTER END ~~~~')

#     party.move(elmos)
#     jezze_move(lockh)
#     print('~~~~ SPRING END ~~~~')

#     party.move(coppr)
#     jezze_move(lockh)
#     print('~~~~ SUMMER END ~~~~')

#     party.move(rootw)
#     jezze_move(lockh)
#     print('~~~~ AUTUMN END ~~~~')