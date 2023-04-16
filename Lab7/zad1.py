from typing import List, Union, Any

def extract_numbers(vals: List[Any]) -> List[Union[int, float]]:
    return list(filter(lambda x: isinstance(x, (int, float)), vals))