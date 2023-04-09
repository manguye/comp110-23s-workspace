"""EX08 - Data Wrangling"""

__author__ = "730411646"

from csv import DictReader

def read_csv_rows(filename:str) -> list[dict[str, str]]:
    """Read an entire CSV of data into a list of rows, each row represented as a dict[str, str]."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close
    return result


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Produce a list[str] of all values in a single column whose name is the second parameter."""
    result: list[str] = []
    for row in table:
        result.append(row[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table represented as a list of rows into one represented as a dictionary of columns."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = table[0]
    for key in first_row:
        result[key] = column_values(table, key)
    return result


def head(table: dict[str, list[str]], number_of_rows: int) -> dict[str, list[str]]:
    """Produce a new column-based table with one the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in table:
        revolving_list: list[int] = []
        if number_of_rows > len(table):
            for idx in range(0, len(table)):
                revolving_list.append(table[column][idx])
        else:
            for idx in range(0, number_of_rows):
                revolving_list.append(table[column][idx])
        result[column] = revolving_list
    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for key in names:
        result[key] = table[key]
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for key in table1:
        result[key] = table1[key]
    for key in table2:
        if key in result:
            result[key] += table2[key]
        else:
            result[key] = table2[key]
    return result


def count(uncounted_values: list[str]) -> dict[str, int]:
    """Given a list[str], will produce a dict[str, int] where each key is a unique value in the given list and each value associated is the value of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    for key in uncounted_values:
        if key in result:
            result[key] += 1
        else:
            result[key] = 1
    return result