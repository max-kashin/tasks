from collections import defaultdict


class CoffeeMachine:
    denominations = [1, 2, 5, 10, 20, 50, 100, 200]  # in cents

    def greedy_get_coins(self, coffee_price: float, eur_inserted: float) -> dict:
        """
        Greedy algorithm, just for comparison
        :param coffee_price:
        :param eur_inserted:
        :return: {coin: number}
        """
        self.validate_input(coffee_price, eur_inserted)

        change = self.get_change(coffee_price, eur_inserted)
        coins_to_return = defaultdict(int)
        for coin in reversed(self.denominations):
            while change >= coin:
                coins_to_return[coin] += 1
                change -= coin
        return coins_to_return

    def return_coins(self, coffee_price: float, eur_inserted: float) -> dict:
        """
        Dynamic solution
        :param coffee_price:
        :param eur_inserted:
        :return:
        """
        self.validate_input(coffee_price, eur_inserted)

        change = self.get_change(coffee_price, eur_inserted)
        used_coin = [0] * (change + 1)
        coins_min = [0] * (change + 1)

        for cents in range(change + 1):
            coin_count = cents
            new_coin = 1
            for value in [c for c in self.denominations if c <= cents]:
                if coins_min[cents - value] + 1 < coin_count:
                    coin_count = coins_min[cents - value] + 1
                    new_coin = value
            coins_min[cents] = coin_count
            used_coin[cents] = new_coin

        coins_to_return = defaultdict(int)

        while change > 0:
            coins_to_return[used_coin[change]] += 1
            change -= used_coin[change]

        return coins_to_return

    @staticmethod
    def get_change(coffee_price: float, eur_inserted: float) -> int:
        return int((eur_inserted - coffee_price) * 100)

    @staticmethod
    def get_human_readable_change_list(change_list: dict):
        cents_to_coins = {
            1: '1 cent',
            2: '2 cent',
            5: '5 cent',
            10: '10 cent',
            20: '20 cent',
            50: '50 cent',
            100: '1 euro',
            200: '2 euro'
        }
        return ", ".join(
            [
                f"{value} {'coin' if value == 1 else 'coins'} of {cents_to_coins[key]}"
                for (key, value)
                in change_list.items()
            ]
        )

    @staticmethod
    def validate_input(coffee_price: float, eur_inserted: float):
        if (
            coffee_price < 0
            or eur_inserted <= 0
            or eur_inserted < coffee_price
        ):
            raise Exception('Incorrect input')


if __name__ == '__main__':
    # test case - ((price, input), expected result)
    test_cases = [
        ((10, 100), {200: 45}),
        ((3.14, 5), {1: 1, 5: 1, 10: 1, 20: 1, 50: 1, 100: 1}),
        ((5, 5), {}),
    ]

    cm = CoffeeMachine()
    for case, expected_result in test_cases:
        actual_result = cm.return_coins(*case)

        assert actual_result == expected_result

        coffee_price, input_eur = case
        print((
            f"For {coffee_price} euro coffee price "
            f"and {input_eur} euro input"
            f" we will get "
            f"{cm.get_human_readable_change_list(actual_result)}\n"
        ))
