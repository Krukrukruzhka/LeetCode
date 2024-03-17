def first_solution(seats: list[int]) -> int:
    """
    Time complexity O(n)
    Space complexity O(1)
    """
    dist = 0
    l, r = 0, 0
    while l < len(seats):
        if seats[l] == 0:
            r = l
            while r < len(seats) and seats[r] == 0:
                r += 1
            if r == len(seats):
                dist = max(dist, r - l)
                break
            else:
                if l == 0:
                    dist = max(dist, r - l)
                dist = max(dist, (r - l) // 2 + (r - l) % 2)
                l = r
        l += 1
    return dist


if __name__ == '__main__':
    input_data = {
        "seats": [1, 0, 0, 0, 1, 0, 1]
    }
    print(first_solution(**input_data))
