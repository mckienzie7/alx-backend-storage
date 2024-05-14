#!/usr/bin/env python3
"""
Insert file
"""


def insert_school(mongo_collection, **kwargs):
    """Function that inset file to the mongodb"""
    data = mongo_collection.insert_one(kwargs)
    return data.inserted_id
