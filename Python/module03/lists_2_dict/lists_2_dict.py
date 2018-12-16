def lists_2_dict(lst_keys, lst_values):
    try:
        dict_result = {elem: lst_values[index] for index, elem in enumerate(lst_keys)}
        print('Result dictionary:', dict_result)
        return dict_result
    except TypeError:
        print('TypeError! Keys:', lst_keys, '| Values:', lst_values)
        raise TypeError
