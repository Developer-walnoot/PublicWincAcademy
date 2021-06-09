from main import *


def test_get_none():
    assert get_none() == None 
    return True

def test_flatten_dict():
    dict = {"a":[12, 12.12], "b":[123, "Meh"]}
    allDictValues = list(dict.values())
    assert flatten_dict(dict) == allDictValues

