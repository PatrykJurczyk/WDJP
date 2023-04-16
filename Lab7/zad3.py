def sort_list(lst, reverse=False):
    nums = sorted([i for i in lst if isinstance(i, int)])
    strings = sorted([i for i in lst if isinstance(i, str)])
    return strings + nums if reverse else nums + strings