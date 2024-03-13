def first_solution(aliceValues: list[int], bobValues: list[int]) -> int:
    """
    Time complexity O(n*log(n)), where n is len(aliceValues) = len(bobValues)
    Space complexity O(n)

    NOTE: that solution can be upgraded using counting sort
    """
    values = sorted([(aliceValues[i], bobValues[i]) for i in range(len(aliceValues))], key=lambda x: x[0]+x[1], reverse=True)
    aliceScore, bobScore = sum([val[0] for val in values[::2]]), sum([val[1] for val in values[1::2]])
    if aliceScore == bobScore:
        return 0
    else:
        return 1 if aliceScore > bobScore else -1


if __name__ == "__main__":
    input_data = {
        "aliceValues": [2, 4, 3],
        "bobValues": [1, 6, 7]
    }

    print(first_solution(**input_data))
