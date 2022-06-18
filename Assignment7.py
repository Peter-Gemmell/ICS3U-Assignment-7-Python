#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on June 2022
# This program calculates tax with list


def find_tax(product_item, product_cost):
    # here is the calculation of tax for multiple items using list
    total = 0
    for loop_counter in range(len(product_item)):
        item = product_item[loop_counter]
        price = product_cost[loop_counter]
        total += price

    tax = total * 0.13
    plus_tax = tax + total

    return plus_tax


def main():

    # This function gets input
    product_item = []
    product_cost = []

    # Input
    try:
        print("Calculates final cost with tax (To finish program click !).\n")
        while True:
            single_product_item = input("Enter product item: ")
            if single_product_item != "!":
                product_item.append(single_product_item)
                single_product_item_cost = float(
                    input("Enter the price of {0}: ".format(single_product_item))
                )
                product_cost.append(single_product_item_cost)
            else:
                tax = find_tax(product_item, product_cost)
                print("\nThe final cost is {0} $.".format(tax))
    except Exception:
        print("\nInvalid input entered, please try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()
