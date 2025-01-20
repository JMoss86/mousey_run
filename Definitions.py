elem = lambda s, a: getattr(s, a, None)

elem_string = lambda e: f' {e}' if e else ''

elem_list = lambda e: e if elem_is_list(e) else [e]

self_elem_list = lambda s, a: elem_list(elem(s, a))

name_elem = lambda s: elem(s, 'name')

elem_is_type = lambda e, t: isinstance(e, t if isinstance(t, type) else type(t))

elem_is_list = lambda e: isinstance(e, list)

elem_is_all = lambda e, t: not e or (elem_is_type(e, t) if not elem_is_list(e) else all(elem_is_all(x, t) for x in e))

name_elem_is_type = lambda s, t: elem_is_type(name_elem(s), t)

has_elem = lambda s, e, a: all(x in self_elem_list(s, a) for x in elem_list(e))

set_elem_unless = lambda f, s, e, a: False if f else setattr(s, a,e) or True

add_elem_list = lambda s, e, a: setattr(s, a, self_elem_list(s, a) + elem_list(e)) if e and not has_elem(s, e, a) else None

sub_elem_list = lambda s, e, a: setattr(s, a, [e for e in self_elem_list(s, a) if e not in elem_list(e)]) if e and has_elem(s, e, a) else None

E = object | None

def validated_elem_list(
    elem: E | list[E] = None,
    elem_type: E | list[E] = None,
    *,
    num_lists: int = 1,
    none_type: E | list[E] = []
) -> list[E | list[E]]:
    '''
    Recursively validates `elem_type` of `elem`/s to any nested list depth.

    Returns `num_lists` `elem` list/s, filling missing input list/s with list/s of `none_type`; minimum one list.
    
    Returns `num_lists` `none_type` list/s, if `elem`/s not all `elem_type`; minimum one list.
    '''
    return ((e := elem_list(elem or none_type if elem_is_all(elem, elem_type) else none_type)) + e * (n := max(0, num_lists - len(e))))[:n + 1]