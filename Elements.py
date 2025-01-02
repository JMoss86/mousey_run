class Element():
    '''
    Is equal to an object if the object's `name` attribute is equal
    to and of the same parent class as its `name` attribute.

    Uses its `name` attribute for `string` representaion.

    Represents itself as its `string` representation.
    '''
    def __eq__(self, other: 'object') -> 'bool':
        if type(self := _get_name(self)) != type(other := _get_name(other)): return False
        return  self == other

    def __repr__(self) -> 'str':
        return self.__str__()

    def __str__(self) -> 'str':
        return f'{_get_name(self)}'

_get_name = lambda e: getattr(e, 'name')

E = Element

def validated_elem_lists(
    elem: 'E | list[E] | list[E | list[E]] | None',
    elem_type: 'E',
    *,
    num_lists: 'int',
    none_type: 'None' = None
) -> 'list[list[E | None]]':
    '''
    Recursively validates all `elem`/s are of `elem_type` to any list depth, counting Falsey values as True.

    Returns `num_lists` list/s of `none_type` if not all `elem`s are valid.

    Returns list of `num_lists` list/s of `elem`/s, replacing Falsey values with `none_type`
    '''
    if not elem and validated_elem(elem, elem_type): return [[none_type] * num_lists]
    return ((elem_list := ensure_list(elem)) + [none_type] * max(0, num_lists - len(elem_list)))[:num_lists]

ensure_list = lambda e: e if isinstance(e, list) else [e]

def validated_elem(
    elem: 'E | list[E] | list[E | list[E]] | None',
    elem_type: 'E',
) -> 'bool':
    '''
    Recursively validates all `elem`/s are of `elem_type` to any list depth, counting Falsey values as True.
    '''
    return (
        not elem or
        not isinstance(elem, list) and is_type(elem, elem_type)
        or all(validated_elem(e, elem_type) for e in elem)
    )

is_type = lambda e, t: issubclass(type(e), t)
