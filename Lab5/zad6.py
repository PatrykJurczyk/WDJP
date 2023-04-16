def foo(* text: str) -> list():
    if len(text) == 0:
        return list()
    else:
        return sorted([ x for x in text ])
    
print(foo('alfa', 'beta', 'a', 'ba', 'bz'))

