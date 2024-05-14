#!/usr/bin/env python3
"""
Insert file
"""


def insert_school(mongo_collection, **kwargs):
    """Function that inset file to the mongodb"""
    arr = []
    for key, value in kwargs.items():
        arr.append({key:value})

    mongo_collection.insert_many(arr)
