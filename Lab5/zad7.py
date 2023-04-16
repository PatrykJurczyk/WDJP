def foo(** teams: dict()) -> int:
    return sum([teams[x] for x in teams])

print(foo(red_bulls = 4, blue_cats = 2, green_panteras = 7)) 