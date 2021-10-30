# duck typing example
from typing import Iterable


def print_items(items: Iterable):
    for item in items:
        print(item)


print_items([1,2,3])
print_items({4, 5, 6})
print_items({"A": 1, "B": 2, "C": 3})
print_items({"A": 1, "B": 2, "C": 3}.values())