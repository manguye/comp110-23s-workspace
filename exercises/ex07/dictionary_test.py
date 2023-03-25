"""Unit tests for the dictionary file in exercise 07."""

__author__ = "730411646"


from exercises.ex07.dictionary import invert, favorite_color, count

def test_single_pair_invert() -> None:
    """Tests invert if input is a single pair dictionary."""
    test_dict: dict[str, str] = {"a", "z"}
    assert invert(test_dict) == {"z", "a"}