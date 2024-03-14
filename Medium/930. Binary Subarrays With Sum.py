def first_solution(nums: list[int], goal: int) -> int:
    """
    Time complexity O(n^2)
    Space complexity O(1)

    NOTE: this solution return TL
    """
    for i in range(1, nums.__len__()):
        nums[i] += nums[i-1]

    subarray_cntr = 0
    for i in range(nums.__len__()):
        if nums[i] == goal:
            subarray_cntr += 1
        for j in range(i):
            if nums[i]-nums[j] == goal:
                subarray_cntr += 1

    return subarray_cntr


def second_solution(nums: list[int], goal: int) -> int:
    """
    Time complexity O(n)
    Space complexity O(n)
    """
    cntr = 0
    zeroes = []
    for i in nums:  # "cntr" is number of zeroes between ones and "nums" boundaries
        if i:
            zeroes.append(cntr)
            cntr = 0
        else:
            cntr += 1
    zeroes.append(cntr)

    answer = 0  # answer calculation
    if goal:
        for i in range(len(zeroes)-goal):
            answer += (zeroes[i] + 1) * (zeroes[i+goal] + 1)
    else:
        for i in zeroes:
            answer += (i+1)*i//2
    return answer


if __name__ == "__main__":
    input_data = {
        "nums": [1, 0, 1, 0, 1],
        "goal": 2
    }
    print(second_solution(**input_data))
