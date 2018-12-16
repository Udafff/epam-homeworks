def multiple_in_range(st_range, en_range):
    lstInterval = [i for i in range(st_range, en_range + 1) if i % 7 == 0 and i % 5 > 0]
    print(lstInterval)
    return lstInterval


# multiple_in_range(1, 77)


# lstInterval = range(1, (77+1))
# print(lstInterval)
#
# for i in lstInterval:
#     print(i, end=' ')
# print()
#
# for i in lstInterval:
#     print(i, end=' ')
#     if (i % 7) == 0:
#         print(i)
#     else:
#         print()
#
# for i in range(1,77+1):
#     if i % 7 == 0 and i % 5 > 0: print(i)
#
# lstInterval = [i for i in range(1,77+1) if i % 7 == 0 and i % 5 > 0]
# print(lstInterval)