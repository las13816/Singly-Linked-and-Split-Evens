from split_evens_odds import SplitEvensOdds


def main():
    sll = SplitEvensOdds()

    sll.build_list_forward([
        1, 2, 3, 4, 5, 6, 7, 8,
        15, 14, 13, 12, 11, 10, 9
    ])

    print(sll.display())

    evens, odds = sll.split()

    print(evens.display())
    print(odds.display())
    print(sll.display())


if __name__ == "__main__":
    main()