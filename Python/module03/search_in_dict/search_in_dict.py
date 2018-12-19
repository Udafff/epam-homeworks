def search_in_dict(search_values, data_set_dict):
    print('Input param, search_values: \n -- search_values=', search_values, '\n -- data_set_dict=', data_set_dict)
    try:
        result = set()

        for s_val in search_values:
            print('Element in "search set", s_val:', s_val)
            for el in data_set_dict.keys():
                print('  Dictionary element=', data_set_dict.get(el), '<==> Search element=', s_val)
                if data_set_dict.get(el) == str(s_val):
                    print('  -- Elements are equal!! ', data_set_dict.get(el), '==', s_val)
                    print()
                    result.add(s_val)

        print()
        print(' -- Set with result: ', result)
        return result

    except TypeError:
        print('TypeError!')
        raise TypeError
    print()


# search_in_dict({'24', 'Kate', 'Developer'}, {'0': 'Ivan', 'Name': 'Kate', '2': 24, '3': '22', '4': 'DevOps', '5': 'Developer'})
# search_in_dict(["1", "2", "1000", "testStr"], {0: 'Ivan', 'Name': 'Kate', 2: 24, 3: 22, 4: 'DevOps', 5: 'Developer', 6:"1", 7:"1000"})