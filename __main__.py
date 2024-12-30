import traceback
from NAME import TOKN as TK, TOWN as TN
from Tokn import Tdum, Tfrn, Tgrd, Tmyr, Tokn, Tpna, Tspy
from Town import Trek

def main():
    lockh = Trek(TN.LOCKHAVEN)
    elmos = Trek(TN.ELMOSS)
    coppr = Trek(TN.COPPERWOOD)
    rootw = Trek(TN.ROOTWALLOW)

    elmos.add_infc()

    stdrd = [coppr, rootw]
    specl = [rootw, elmos]

    agnts = [
        party := Tgrd(TK.PARTY),
        jezze := Tokn(TK.JEZZEBELLE)
    ]
    tokns = [
        justn := Tdum(TK.JUSTIN, specl),
        mtrap := Tgrd(TK.MOUSETRAP, stdrd),
        trevr := Tgrd(TK.TREVER, specl),
        charl := Tmyr(TK.CHARLES, stdrd, agnts),
        rabbt := Tfrn(TK.RABBIT, stdrd),
        creek := Tspy(TK.CREEK, stdrd[::-1]),
        panac := Tpna(TK.PANACEA, specl)
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