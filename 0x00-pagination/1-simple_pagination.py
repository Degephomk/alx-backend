#!/usr/bin/env python3

"""
1-simple_pagination
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Takes two integer arguments page and page_size.
    """
    index_tuple = page_size * (page - 1), page * page_size
    return index_tuple


class Server:
    """Server class to paginate.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """init object"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        paginate 
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        indexes = index_range(page, page_size)
        try:
            data = self.dataset()
            return data[indexes[0]: indexes[1]]
        except IndexError:
            return []
