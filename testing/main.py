def get_none():
    return None

def flatten_dict(dictionary):
    EntireList = []
    for pair in dictionary:
        list = dictionary[pair]
        EntireList.append(list)
    return EntireList


