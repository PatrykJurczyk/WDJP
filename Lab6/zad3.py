def find_n_values(lst, n, reverse=False):
    if not all(isinstance(x, (int, float)) for x in lst):
        raise TypeError("The list should contain only numbers.")

    return sorted(lst, reverse=reverse)[:n] if not reverse else sorted(lst)[:n]

lst = [5, 10, 2, 8, 3]
print(find_n_values(lst, 3))