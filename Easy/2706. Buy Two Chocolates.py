def first_solution(prices: list[int], money: int) -> int:
    """
    Time complexity O(n)
    Space complexity O(1)
    """
    price1, price2 = 500, 500
    for price in prices:
        if price <= price1:
            price1, price2 = price, price1
        elif price < price2:
            price2 = price

    if money >= price1 + price2:
        return money - (price1 + price2)
    else:
        return money


if __name__ == "__main__":
    input_data = {
        "prices": [3, 2, 3],
        "money": 3
    }
    print(first_solution(**input_data))
