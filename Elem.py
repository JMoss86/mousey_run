class Element():
    def __eq__(self, other: object) -> bool:
        return self.__repr__() == other.__repr__()

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return getattr(self, 'name')