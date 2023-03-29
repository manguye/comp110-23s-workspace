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

