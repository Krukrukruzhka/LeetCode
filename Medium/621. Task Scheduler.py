def first_solution(tasks: list[str], n: int) -> int:
    """
    Time complexity O(n)
    Space complexity O(n)
    """
    d: dict[str, int] = dict()
    for i in tasks:
        d[i] = d.get(i, 0) + 1

    cntrs: list[int] = sorted(d.values(), reverse=True)
    del d
    res, null_cntr = 0, (n + 1) * (cntrs[0] - 1)
    for cntr in cntrs:
        res += cntr
        if cntr == cntrs[0]:
            null_cntr -= cntr - 1
        else:
            null_cntr -= cntr
    return res + (null_cntr if null_cntr > 0 else 0)


if __name__ == '__main__':
    input_data = {
        "tasks": ["A", "A", "A", "B", "B", "B"],
        "n": 3
    }
    print(first_solution(**input_data))
