#!/usr/bin/python

import argparse
# [1050, 270, 1540, 3800, 2]  --> 3530

#    prices.sort()
#    a = prices[0]
#    b = prices[-1]
#    return b - a
#
# print(find_max_profit([1050, 270, 1540, 3800, 2]))

# prices = [1050, 270, 1540, 3800, 2]

def find_max_profit(prices):

    big_num = 0
    small_num = None
    new_list = []

    for i in range(0, len(prices)):

      if prices[0] == big_num:
        big_num = prices[1]
        small_num = big_num
        new_list = prices[:i]
      elif prices[i] > big_num:
        big_num = prices[i]
        small_num = big_num
        new_list = prices[:i]

    # print(big_num)
    # print(small_num)
    # print(new_list)

    for j in range(0, len(new_list)):
      if new_list[j] < small_num:
        small_num = new_list[j]
      elif new_list[j] == new_list[0]:
        small_num = new_list[j]

    return big_num - small_num


# print(find_max_profit([100, 90, 80, 50, 20, 10])) #[100, 90, 80, 50, 20, 10] --- [1050, 270, 1540, 3800, 2]



# we want to iterate through (loop) the List(prices) and find thew biggest number
# [3800]

# save/hold biggest number
# big_num = [3800]

# then make a new list with the biggest number as the end
# new_list = [prices[0]:big_num]

# we want to iterate through (loop) the new List(new_list) to find the smallest number
# new_list = [1050, 270, 1540, 3800]
# [270]

# save/hold smallest number
# small_num = [270]

# we want to return smallest number subtracted from the biggest number
# return big_num - small_num



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))