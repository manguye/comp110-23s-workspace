"""Unit tests for the dictionary file in exercise 07."""

__author__ = "730411646"


from dictionary import invert, favorite_color, count
import pytest

def test_single_pair_invert() -> None:
    """Tests invert if input is a single pair dictionary."""
    test_dict: dict[str, str] = {"apple": "cat"}
    assert invert(test_dict) == {"cat": "apple"}


def test_multiple_pairs_invert() -> None:
    """Tests invert if input is a dictionary with multiple pairs."""
    test_dict: dict[str, str] = {"a": "z", "b": "y", "c": "x"}
    assert invert(test_dict) == {"z": "a", "y": "b", "x": "c"}


def test_one_color_favorite_color() -> None:
    """Tests favorite_color if input is a dictionary with the same values."""
    test_dict: dict[str, str] = {"Adam": "green", "Bart": "green", "Charles": "green"}
    assert favorite_color(test_dict) == "green"


def test_two_colors_favorite_color() -> None:
    """Tests favorite_color if input is a dictionary with different numbers of different values."""
    test_dict: dict[str, str] = {"Adam": "green", "Bart": "blue", "Charles": "blue"}
    assert favorite_color(test_dict) == "blue"


def test_equal_colors_favorite_color() -> None:
    """Tests favorite_color if input is a dictionary with equal number of different values."""
    test_dict: dict[str ,str] = {"Adam": "green", "Bart": "green", "Charles": "blue", "David": "blue"}
    assert favorite_color(test_dict) == "green"

def test_empty_count() -> None:
    """Tests count if input is an empty list."""
    test_list: list[str] = []
    assert count(test_list) == {}

def test_equal_count() -> None:
    """Tests count if input contains an equal number of unique objects in sequential order."""
    test_list: list[str] = ["apple", "apple", "apple", "banana", "banana", "banana", "cantaloupe", "cantaloupe", "cantaloupe"]
    assert count(test_list) == {"apple": 3, "banana": 3, "cantaloupe": 3}