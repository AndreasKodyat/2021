print("Stock Estimator")

stock_name = input("Stock name: ")
print("Enter first week Open,Highest,Lowest,Close price: ")
open_1,high_1,low_1,close_1 = [int(x) for x in input().split()]

print("Enter second week Open,Highest,Lowest,Close price: ")
open_2,high_2,low_2,close_2 = [int(x) for x in input().split()]

print("\nResult : ")
print("Week 1: ", open_1,high_1,low_1,close_1)
print("Week 2: ", open_2,high_2,low_2,close_2)

open_diff = open_2-open_1
high_diff = high_2-high_1
low_diff = low_2-low_1
close_diff = close_2-close_1

print(stock_name, open_diff, high_diff, low_diff, close_diff)