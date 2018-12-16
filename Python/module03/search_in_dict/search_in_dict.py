def search_in_dict(search_values, data_set_dict):
    try:
        result = set()

        for s_val in search_values:
            for el in data_set_dict.keys():
                if data_set_dict.get(el) == s_val:
                    print(s_val)
                    result.add(s_val)
        print(result)
        return result

    except TypeError:
        print('TypeError!')
        raise TypeError


# search_in_dict([24, 'Kate', 'Developer'], {0: 'Ivan', 'Name': 'Kate', 2: 24, 3: 22, 4: 'DevOps', 5: 'Developer'})
# search_in_dict(["1", "2", "1000", "testStr"], {0: 'Ivan', 'Name': 'Kate', 2: 24, 3: 22, 4: 'DevOps', 5: 'Developer', 6:"1", 7:"1000"})