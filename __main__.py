import traceback
from NAME import TOKN, TOWN
from Tokn import Tdum, Tfrn, Tgrd, Tmyr, Tokn, Tpna, Tspy
from Town import Trek

def main():
    lockh = Trek(TOWN.LOCKHAVEN)
    elmos = Trek(TOWN.ELMOSS)
    coppr = Trek(TOWN.COPPERWOOD)
    rootw = Trek(TOWN.ROOTWALLOW)

    elmos.add_infc()

    stdrd = [coppr, rootw]
    specl = [rootw, elmos]

    agnts = [
        party := Tgrd(TOKN.PARTY),
        jezze := Tokn(TOKN.JEZZEBELLE)
    ]
    tokns = [
        justn := Tdum(TOKN.JUSTIN, specl),
        mtrap := Tgrd(TOKN.MOUSETRAP, stdrd),
        trevr := Tgrd(TOKN.TREVER, specl),
        charl := Tmyr(TOKN.CHARLES, stdrd, agnts),
        rabbt := Tfrn(TOKN.RABBIT, stdrd),
        creek := Tspy(TOKN.CREEK, stdrd[::-1]),
        panac := Tpna(TOKN.PANACEA, specl)
    ]

    for tgrd in [party, mtrap, trevr]:
        tgrd.set_base(lockh)

    lockh.add_tkns([
        party,
        jezze,
        justn,
        mtrap,
        creek,
        panac
    ])
    elmos.add_tkns(charl)
    coppr.add_tkns(trevr)
    rootw.add_tkns(rabbt)

    def display() -> str: print(f'~~~~\n{lockh}\n\n{elmos}\n\n{coppr}\n\n{rootw}\n~~~~')
    def move(tokns: list[Tokn]) -> None:
        for tokn in tokns:
            tokn.move()
            display()
    def rset(tokns: list[Tokn]) -> None:
        for tokn in tokns:
            tokn.rset()
            display()

    display()
    print('~~~~ WINTER END ~~~~')

    party.move(elmos)
    display()
    jezze.move(lockh)
    display()
    move(tokns)

    party.rset()
    display()
    jezze.move(lockh)
    display
    rset(tokns)
    print('~~~~ SPRING END ~~~~')

    party.move(coppr)
    display()
    jezze.move(lockh)
    display()
    move(tokns)

    party.rset()
    display()
    jezze.move(lockh)
    display
    rset(tokns)
    print('~~~~ SUMMER END ~~~~')

    party.move(rootw)
    display()
    jezze.move(lockh)
    display()
    move(tokns)

    party.rset()
    display()
    jezze.move(lockh)
    display
    rset(tokns)
    print('~~~~ AUTUMN END ~~~~')

if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(traceback.format_exc())