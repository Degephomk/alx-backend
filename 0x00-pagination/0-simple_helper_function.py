#!/usr/bin/env python3

"""
Write a function named index_range that takes two integer
"""

def index_range(page: int, page_size: int) -> tuple:
    
    index_tuple = page_size * (page - 1), page * page_size
    return index_tuple
