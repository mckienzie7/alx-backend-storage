#!/usr/bin/env python3
"""
Python code that list all document in the mogodb collection
"""


def list_all(mongo_collection):
    """function that return list of documents"""
    listone = []
    for lis in mongo_collection.find():
        listone.append(lis)
    if len(listone) != 0:
        return listone
    return []
