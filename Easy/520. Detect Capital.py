def first_solution(word: str) -> bool:
    """
    Time complexity O(n), where n is word's length
    Space complexity O(n). We use an additional memory for slices and lower/upper functions
    """
    return word == word.upper() or word[1:] == word[1:].lower()


def second_solution(word: str) -> bool:
    """
    Time complexity O(n), where n is word's length
    Space complexity O(1)
    """
    def is_uppercase(character: str) -> bool:
        return 'A' <= character <= 'Z'

    if len(word) <= 1:
        return True
    if not is_uppercase(word[0]) and is_uppercase(word[1]):
        return False

    for i in range(2, len(word)):
        if not is_uppercase(word[0]) and is_uppercase(word[i]):
            return False
        if is_uppercase(word[0]) and (is_uppercase(word[1]) != is_uppercase(word[i])):
            return False

    return True


if __name__ == "__main__":
    input_data = {
        "word": input()
    }
    print(second_solution(**input_data))
