def filter_by_state(dict_list : list, key: str = "EXECUTED") -> list:
    new_dict = []
    for dict in dict_list:
        if dict["state"] == key:
            new_dict.append(dict)
    return new_dict

def sort_by_date(dict_list : list, sort_by: str) -> list:
    pass