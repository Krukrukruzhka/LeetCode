def first_solution(properties: list[list[int]]) -> int:
    """
    Time complexity O(n*log(n)), where n = len(properties)
    Space complexity O(n)

    NOTE: this solution return TL
    """

    properties = sorted(sorted(properties, key=lambda x: x[1], reverse=True), key=lambda x: x[0], reverse=True)

    cntr = 0
    current_max, next_max = properties[0], properties[0]

    for card_index in range(1, properties.__len__()):
        if properties[card_index][0] < properties[card_index - 1][0]:
            current_max = next_max
            next_max = properties[card_index] if properties[card_index][1] > next_max[1] else next_max
        if properties[card_index][0] < current_max[0] and properties[card_index][1] < current_max[1]:
            cntr += 1

    return cntr


if __name__ == "__main__":
    input_data = {
        "properties": [[1, 5], [10, 4], [4, 3]]
    }
    print(first_solution(**input_data))
