from Definitions import  name_elem, elem_is_type

class Element():
    def __str__(self) -> str:
        return f'{name_elem(self)}'
    
    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        return elem_is_type(self_name := name_elem(self), name_elem(other)) or elem_is_type(self_name, other)

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)