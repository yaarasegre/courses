#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import numpy as np
from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    taken, value, optimal = lp(capacity, items)

    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(optimal) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data

# def bnb(capacity, items):
#     items_wieght_density = np.empty(len(items))
#     for i, item in enumerate(items):
#         items_wieght_density[i] = float(item.weight) / item.value
#     items_order = items_wieght_density.argsort()
#     ordered_wieght_density = items_wieght_density[items_order]
#
#     value = 0
#     taken = [0] * len(items)
#     optimal = 0
#     return taken, value, optimal

# def linear_relaxation(capacity, items):


def greedy(capacity, items):
    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0] * len(items)
    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight
    return taken, value


def lp(capacity, items, max_seconds = 3600*5):

    n = len(items)

    # # linear programming
    # start = datetime.datetime.now()
    # max_time = datetime.timedelta(seconds=60 - 3)
    #
    # # order by value density
    # items_weight_density = np.empty(len(orig_items))
    # for i, item in enumerate(orig_items):
    #     items_weight_density[i] = float(item.weight) / item.value
    # order = range(len(items_weight_density))
    # order.sort(key=items_weight_density.__getitem__, reverse=True)
    #
    # items = sorted(orig_items, reverse=True)

    mat = np.zeros(shape=(capacity+1, len(items)+1))
    for i_item in range(len(items)):
        # if i_item % 10 == 1:
            # print('{} out of {}'.format(i_item, len(items)))
        curr_value = items[i_item].value
        curr_weight = items[i_item].weight
        for curr_capacity in range(1, capacity+1):
            if curr_weight > curr_capacity:
                # item doesn't fit
                mat[curr_capacity, i_item+1] = mat[curr_capacity, i_item]
            else:
                value_with_item = mat[curr_capacity - curr_weight, i_item] + curr_value
                if value_with_item > mat[curr_capacity, i_item]:
                    # take item
                    mat[curr_capacity, i_item+1] = value_with_item
                else:
                    # skip item
                    mat[curr_capacity, i_item+1] = mat[curr_capacity, i_item]
    # print('capacity ' + str(capacity))
    # print(items)
    # print(mat)
    optimal = 1

    # unsort
    taken, value = trace_back(mat, capacity, items)
    # taken = [0] * n
    # for i, c in zip(order, sorted_taken):
    #     taken[i] = c
    return taken, value, optimal


def trace_back(mat, capacity, items):
    n_items = len(items)
    value = int(mat[capacity, len(items)])
    taken = [0] * n_items
    row = capacity
    # item_i is 1 based
    for item_i in range(n_items, 0, -1):
        if mat[row, item_i] == mat[row, item_i-1]:
            taken[item_i-1] = 0
            # row unchanged
        else:
            taken[item_i-1] = 1
            row -= items[item_i-1].weight

    return taken, value


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

