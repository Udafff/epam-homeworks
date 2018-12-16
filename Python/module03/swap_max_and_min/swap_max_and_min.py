def swap_max_and_min(lst_numbers):
    try:
        if len(lst_numbers) != len(set(lst_numbers)):
            raise ValueError

        min_elem = [lst_numbers[0],0]
        max_elem = [lst_numbers[0],0]

        for index, elem in enumerate(lst_numbers):
            if not isinstance(elem, int):
                raise TypeError

            if elem < min_elem[0]:
                min_elem = [elem, index]

            if elem > max_elem[0]:
                max_elem = [elem, index]

        print('Orig list:', lst_numbers, end=' ==> ')
        lst_numbers[min_elem[1]], lst_numbers[max_elem[1]] = lst_numbers[max_elem[1]], lst_numbers[min_elem[1]]
        print('New  list:', lst_numbers)

        return lst_numbers

    except TypeError:
        print("TypeError!, list:", lst_numbers)
        raise TypeError

    except ValueError:
        print("ValueError!, list:", lst_numbers)
        raise ValueError
