def dict_swap(dic):
    try:
        return {dic[i]: i for i in dic.keys()}
    except TypeError:
        print('TypeError!,', dic)
        raise TypeError
