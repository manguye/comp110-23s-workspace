"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730411646"


class Simpy:
    """Everything you might every want or need for Simpy."""

    values: list[float]

    def __init__(self, number_list: list[float]):
        """Initializes a new Simpy object."""
        self.values = number_list

    def __str__(self) -> str:
        """Makes printing Simpy prettier."""
        return f"Simpy({self.values})"
    
    def fill(self, number: float, how_much: int) -> None:
        """Fills Simpy.values with a specific number of repeating values."""
        new_values: list[float] = []
        while how_much > 0:
            new_values.append(number)
            how_much -= 1
        self.values = new_values

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills in Simpy.values with range of values in terms of floats."""
        assert step != 0
        number: float = start
        while number != stop:
            self.values.append(number)
            number += step

    def sum(self) -> float:
        """Sums the floats in Simpy.values through delegation."""
        final_value: float = sum(self.values)
        return final_value
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overrides add to allow addition between Simpy objects and/or floats."""
        new_simpy: Simpy = Simpy([])
        if isinstance(rhs, float):
            for x in range(0, len(self.values)):
                new_simpy.values.append(self.values[x] + rhs)
        else:  
            assert len(self.values) == len(rhs.values)
            for x in range(0, len(self.values)):
                new_simpy.values.append(self.values[x] + rhs.values[x])
        return new_simpy
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overrides power to allow exponentiation between Simpy objects and/or floats."""
        new_simpy: Simpy = Simpy([])
        if isinstance(rhs, float):
            for x in range(0, len(self.values)):
                new_simpy.values.append(self.values[x] ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for x in range(0, len(self.values)):
                new_simpy.values.append(self.values[x] ** rhs.values[x])
        return new_simpy
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Returns a list of bools that filters Simpy objects if they match other Simpy objects or floats."""
        checklist: list[bool] = []
        if isinstance(rhs, float):
            for x in range(0, len(self.values)):
                if self.values[x] == rhs:
                    checklist.append(True)
                else:
                    checklist.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            for x in range(0, len(self.values)):
                if self.values[x] == rhs.values[x]:
                    checklist.append(True)
                else:
                    checklist.append(False)
        return checklist
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Returns a list of bools that filters Simpy objects if they are greater than other Simpy objects or floats."""
        checklist: list[bool] = []
        if isinstance(rhs, float):
            for x in range(0, len(self.values)):
                if self.values[x] > rhs:
                    checklist.append(True)
                else:
                    checklist.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            for x in range(0, len(self.values)):
                if self.values[x] > rhs.values[x]:
                    checklist.append(True)
                else:
                    checklist.append(False)
        return checklist
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Allows the user to read specific items from the Simpy array."""
        if isinstance(rhs, int):
            requested_number: float = self.values[rhs]
            return requested_number
        else:
            new_simpy: Simpy = Simpy([])
            for x in range(0, len(self.values)):
                if rhs[x]:
                    new_simpy.values.append(self.values[x])
            return new_simpy

    # TODO: Your constructor and methods will go here.