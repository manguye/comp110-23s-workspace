"""Unit tests for utils file in exercise 5."""

__author__ = "730411646"


from exercises.ex05.utils import only_evens, sub, concat


def test_empty_only_evens() -> None:
    """Tests only_evens if input is an empty list."""
    assert only_evens([]) == list()


def test_evens_only_evens() -> None:
    """Tests only_evens if input is a list with only evens."""
    test_list: list[int] = [0, 2, 4, 6]
    assert only_evens(test_list) == [0, 2, 4, 6]


def test_odds_only_evens() -> None:
    """Tests only_evens if input is a list with only odds."""
    test_list: list[int] = [1, 3, 5, 7]
    assert only_evens(test_list) == list()


def test_mixed_only_evens() -> None:
    """Tests only_evens if input is a list with mixed integers."""
    test_list: list[int] = [1, 2, 3, 4]
    assert only_evens(test_list) == [2, 4]


def test_both_empty_concat() -> None:
    """Tests concat if input is two empty lists."""
    assert concat([], []) == list()


def test_one_empty_concat() -> None:
    """Tests concat if input is one empty list and one list with integers."""
    test_list1: list[int] = list()
    test_list2: list[int] = [0, 5, 9, 8]
    assert concat(test_list1, test_list2) == [0, 5, 9, 8]


def test_no_empty_concat() -> None:
    """Tests concat if input is two lists with integers."""
    test_list1: list[int] = [3, 10, 15, 1]
    test_list2: list[int] = [0, 5, 9, 8]
    assert concat(test_list1, test_list2) == [3, 10, 15, 1, 0, 5, 9, 8]


def test_sub_empty() -> None:
    """Tests sub if input is an empty list with range from 0 to length of the list."""
    test_list: list[int] = list()
    x: int = 0
    y: int = len(test_list)
    assert sub(test_list, x, y) == list()


def test_sub_from_2_to_5() -> None:
    """Tests sub if input is a list with integers and with a range from 2 to 5."""
    test_list: list[int] = [1, 2, 3, 5, 8, 13, 21]
    x: int = 2
    y: int = 5
    assert sub(test_list, x, y) == [3, 5, 8]


def test_sub_over() -> None:
    """Tests sub if input is a list with integers and with a range from 0 to 10."""
    test_list: list[int] = [1, 2, 3, 5, 8, 13, 21]
    x: int = 0
    y: int = 10
    assert sub(test_list, x, y) == [1, 2, 3, 5, 8, 13, 21]