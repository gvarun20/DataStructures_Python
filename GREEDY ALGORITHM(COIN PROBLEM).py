# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 23:01:46 2024

@author: varung
"""
def greedy_coin_change(coins, target_amount):
    coins.sort(reverse=True)  # Sort coins in descending order

    num_coins = 0
    current_amount = target_amount
    coin_count = {}

    for coin in coins:
        num_of_coins = current_amount // coin
        coin_count[coin] = num_of_coins
        num_coins += num_of_coins
        current_amount %= coin

    return num_coins, coin_count

# Example usage:
coins = [25, 10, 5, 1]  # Available coin denominations (quarters, dimes, nickels, pennies)
target_amount = 49  # Target amount to make change for

total_coins, coin_distribution = greedy_coin_change(coins, target_amount)

print(f"Minimum number of coins needed: {total_coins}")
print("Number of each coin denomination:")
for coin, count in coin_distribution.items():
    print(f"{coin} cents: {count} coins")

