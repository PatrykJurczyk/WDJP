def sort_dict(d: dict, func: callable) -> dict:
    return dict(sorted(d.items(), key=lambda x: func(x[1])))