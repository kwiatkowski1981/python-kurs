
list_1 = [2, 4, 6]
list_2 = [8, 6, 4]


def sum_list(a: int, b: int) -> int:
    result = []
    for (i, j) in zip(list_1, list_2):
        result.append(i + j)
    return result


print(sum_list(list_1, list_2))

