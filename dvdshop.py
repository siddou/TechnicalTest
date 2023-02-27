#! /usr/bin/env python3
"""deal super smart avec une boutique de vente de DVDs"""

import re

FILE = 'Back-to-the-Future.txt'
TRILOGY = 'Back to the Future'
SINGLE_BTTF_PRICE = 15  # price for a single DVD part of the Back ot the Future Trilogy
DVD_PRICE = 20  # price for a single DVD
TEN_PERCENT_PROMO = 0.9  # 10% discount for 2 different BTTF DVD
TWENTY_PERCENT_PROMO = 0.8  # 20% discount for 3 different BTTF DVD


def main():
    """main.

    """
    try:
        with open(FILE, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            dvdprice = [DVD_PRICE for line in lines  # used to store DVDs price
                        if line != '\n'  # skip empty lines
                        and not re.search(f'{TRILOGY}.+', line)]  # skip BTTF titles
            btf_counts = [0, 0, 0]  # BTTF titles count list
            for line in lines:
                if re.search(f'{TRILOGY}.+', line):  # search for BTTF titles and increase count
                    for i in range(3):
                        if line in [f'{TRILOGY} {i+1}\n', f'{TRILOGY} {i+1}']:
                            btf_counts[i] += 1
    except IOError:
        print('File not found!')
    finally:
        file.close()
    total_price = calculate_total(dvdprice, btf_counts)
    print(int(total_price))


def calculate_total(dvdprice, btf_counts):
    """This function calculate the total price.

    """
    count = len([i for i in btf_counts if i > 0])  # # count values in btf_counts
    b2tfprice = {
        0: 0,  # no BTTF DVD in this order
        1: (sum(btf_counts) * SINGLE_BTTF_PRICE),  # 1 BTTF movie, no discount
        2: ((sum(btf_counts) * SINGLE_BTTF_PRICE) * TEN_PERCENT_PROMO),  # 2 different BTTF movie, 10% discount applied
        3: ((sum(btf_counts) * SINGLE_BTTF_PRICE) * TWENTY_PERCENT_PROMO),  # 3 different BTTF movie, 20% discount applied
    }[count]
    total_price = sum(dvdprice) + b2tfprice
    return int(total_price)


def test_calculate_total():
    assert calculate_total([0], [1, 1, 1]) == 36  # Example n°1
    assert calculate_total([0], [1, 0, 1]) == 27  # Example n°2
    assert calculate_total([0], [1, 0, 0]) == 15  # Example n°3
    assert calculate_total([0], [1, 2, 1]) == 48  # Example n°4
    assert calculate_total([20], [1, 1, 1]) == 56  # Example n°5


if __name__ == '__main__':
    main()
