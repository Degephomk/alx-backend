#!/usr/bin/env python3

"""
Write a function named index_range that takes two integer
"""

def index_range(page: int, page_size: int) -> tuple:

    """
    Write a function named index_range that takes two integer arguments page 
    function should return a tuple of size two containing a start index 
    """
    
    index_tuple = page_size * (page - 1), page * page_size
    return index_tuple
