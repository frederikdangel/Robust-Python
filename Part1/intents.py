from collections import defaultdict, Counter
from typing import List


class Cookbook:
    def __init__(self):
        self.author = None

    pass


def create_author_count_mapping(cookboks: List[Cookbook]):
    counter = defaultdict(lambda: 0)
    for cookbook in cookboks:
        counter[cookbook.author] += 1
    return counter


def create_author_count_mapping2(cookbooks: List[Cookbook]):
    return Counter(book.author for book in cookbooks)
