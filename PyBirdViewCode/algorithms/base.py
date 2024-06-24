from typing import List


def lists_of_bool_union(lists: List[List[bool]]):
    first = lists[0]
    for item in lists[1:]:
        first = list_of_bool_pair_union(first, item)
    return first


def list_of_bool_pair_union(list1: List[bool], list2: List[bool]) -> List[bool]:
    """
    对两个相同长度的List[bool]每一项求交
    """
    assert len(list1) == len(list2)
    return [x or y for x, y in zip(list1, list2)]


def list_of_bool_pair_diff(list1: List[bool], list2: List[bool]) -> List[bool]:
    """
    对两个相同长度的List[bool]每一项求差

    真值表：
    x=1, y=1 --> 0
    x=1, y=0 --> 1
    x=0, y=1 --> 0
    x=0, y=0 --> 0
    """
    assert len(list1) == len(list2)
    return [x and (not y) for x, y in zip(list1, list2)]


def bool_list_to_str(bl: List[bool]):
    return "".join(["1" if item else "0" for item in bl])
