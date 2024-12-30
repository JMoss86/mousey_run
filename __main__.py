import traceback
from NAME import TOKN as TK, TOWN as TN
from Tokn import Tdum, Tfrn, Tgrd, Tmyr, Tpna, Tspy
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
        jezze := Tgrd(TK.JEZZEBELLE)
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

    for tgrd in [party, jezze, mtrap, trevr]:
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

    def display() -> None:
        print(f'~~~~\n{lockh}\n\n{elmos}\n\n{coppr}\n\n{rootw}\n~~~~')
    def move_jezze(trek: Trek) -> None:
        display()
        jezze.move(trek)
        display()
    def move() -> None:
        for tokn in tokns:
            tokn.move()
            display()
    def rset() -> None:
        for agnt in agnts:
            agnt.rset()
            display()
        for tokn in tokns:
            tokn.rset()
            display()
    def run_season(trek: Trek) -> None:
        move_jezze(trek)
        move()
        rset()

    display()
    print('~~~~ WINTER END ~~~~')

    party.move(elmos)
    run_season(lockh)
    print('~~~~ SPRING END ~~~~')

    party.move(coppr)
    run_season(lockh)
    print('~~~~ SUMMER END ~~~~')

    party.move(rootw)
    run_season(lockh)
    print('~~~~ AUTUMN END ~~~~')

if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(traceback.format_exc())