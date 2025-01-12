elem = lambda s, a: getattr(s, a, None)

elem_string = lambda e: f' {e}' if e else ''

elem_list = lambda e: e if elem_is_list(e) else [e]

name_elem = lambda s: elem(s, 'name')

num_lists_elem_list = lambda e, n, z: ((e := elem_list(e or z)) + minimum_num_elem_lists(z, 0, n - len(e)))[:n]

minimum_num_elem_lists = lambda e, m, n: elem_list(e) * max(m, n)

elem_is_list = lambda e: isinstance(e, list)

elem_is_not_list = lambda e: not elem_is_list(e)

elem_is_type = lambda e, t: issubclass(type(e), t or type(t))

elem_is_any = lambda e, t: elem_is_type(e, t) if elem_is_not_list(t) else any(elem_is_type(e, x) for x in t)

elem_is_valid = lambda e, t:  not e or (elem_is_not_list(e) and elem_is_any(e, t)) or all(elem_is_valid(x, t) for x in e)

name_elem_is_type = lambda s, t: elem_is_type(name_elem(s), t)

has_elem = lambda s, e, a: all(x in elem_list(elem(s, a)) for x in elem_list(e))

add_elem = lambda s, e, a: setattr(s, a, elem_list(elem(s, a)) + elem_list(e))

sub_elem = lambda s, e, a: setattr(s, a, [x for x in elem_list(elem(s, a)) if x not in elem_list(e)])

E = object | None

def validated_elem_list(
    elem: E | list[E] = None,
    elem_type: E | list[E] = None,
    *,
    num_lists: int = 1,
    none_type: E | list[E] = [],
    invalid_type: E | list[E] = []
) -> list[E | list[E]]:
    '''
    Recursively validates `elem_type` of `elem`/s to any nested list depth.

    Returns `num_lists` `elem` list/s, filling missing input list/s with list/s of `none_type`; minimum one list.
    
    If `elem`/s not valid `elem_type`; returns `num_lists` 'invalid_type' list/s; minimum one list.
    '''
    if elem_is_valid(elem, elem_type): return num_lists_elem_list(elem, max(1, num_lists), none_type)
    return minimum_num_elem_lists(invalid_type, 1, num_lists)

def add_elem_list(
    self,
    elem: E | list[E],
    attr_name: str
) -> None:
    if elem and not has_elem(self, elem, attr_name): add_elem(self, elem, attr_name)

def sub_elem_list(
    self,
    elem: E | list[E],
    attr_name: str
) -> 'None':
    if elem and has_elem(self, elem, attr_name): sub_elem(self, elem, attr_name)