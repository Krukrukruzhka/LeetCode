def first_solution(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    """
    Time complexity O(n)
    Space complexity O(n)

    NOTE1: the spatial complexity can be O(1) if you remove the slices
    NOTE2: you can apply non-asymptotic transformations by replacing linear search with binary search
    """
    l_start, r_end = -1, -1
    for i in range(intervals.__len__()):
        if intervals[i][1] < newInterval[0]:
            l_start = i
        if intervals[i][0] <= newInterval[1]:
            r_end = i

    l_start += 1
    if l_start == len(intervals):
        return intervals + [newInterval]
    if r_end == -1:
        return [newInterval] + intervals
    if r_end < l_start:
        return intervals[:l_start] + [newInterval] + intervals[l_start:]

    intervals[l_start][0] = min(intervals[l_start][0], newInterval[0])
    intervals[l_start][1] = max(intervals[r_end][1], newInterval[1])
    for i in range(r_end, l_start, -1):
        del intervals[i]
    return intervals


if __name__ == "__main__":
    input_data = {
        "intervals": [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
        "newInterval": [4, 8]
    }
    print(first_solution(**input_data))
