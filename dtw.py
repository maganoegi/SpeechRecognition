

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

# --------------------------------------------------------------- Functions
def distance_cost_plot(distances, plt):
    im = plt.imshow(distances, interpolation='nearest', cmap='Reds')
    plt.gca().invert_yaxis()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.colorbar()

def path_cost(x, y, accumulated_cost, distances):
    path = [[len(x)-1, len(y)-1]]
    cost = 0
    i = len(y)-1
    j = len(x)-1
    while i>0 and j>0:
        if i==0:
            j = j - 1
        elif j==0:
            i = i - 1
        else:
            if accumulated_cost[i-1, j] == min(accumulated_cost[i-1, j-1], accumulated_cost[i-1, j], accumulated_cost[i, j-1]):
                i = i - 1
            elif accumulated_cost[i, j-1] == min(accumulated_cost[i-1, j-1], accumulated_cost[i-1, j], accumulated_cost[i, j-1]):
                j = j-1
            else:
                i = i - 1
                j= j- 1
        path.append([j, i])
    path.append([0,0])
    for [y, x] in path:
        cost += distances[x, y]
    # path_x = [point[0] for point in path]
    # path_y = [point[1] for point in path]
    # plt.plot(path_x, path_y);
    path.reverse()
    return path, cost

# ----------------------------------------------------------------- Main
def dtw(array1, array2):

    dtw_trace = 0
    args = sys.argv
    if len(args) == 2:
        dtw_trace = 1

    x = array1
    y = array2

    # x = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0])
    # y = np.array([0, 0, 0, 0, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    # idx = np.linspace(0, 4.0 * np.pi, 200)
    # idy = np.linspace(0, 4.0 * np.pi,  200)
    # x = np.sin(idx + 5.0)
    # y = np.cos(idy)

    # f1 = plt.figure(1)
    # plt.plot(x,'r', label='x')
    # plt.plot(y, 'g', label='y')
    # plt.legend()
    # # plt.show()

    distances = np.zeros((len(y), len(x)))


    for i in range(len(y)):
        for j in range(len(x)):
            distances[i,j] = (x[j]-y[i])**2

    # print(distances, end="\n\n")
    # f2 = plt.figure(2)
    # distance_cost_plot(distances, plt)

    accumulated_cost = np.zeros((len(y), len(x)))
    for i in range(1, len(x)): # horizontal
        accumulated_cost[0,i] = distances[0,i] + accumulated_cost[0, i-1]

    for i in range(1, len(y)): # vertical
        accumulated_cost[i,0] = distances[i, 0] + accumulated_cost[i-1, 0]

    for i in range(1, len(y)): # all other
        for j in range(1, len(x)):
            accumulated_cost[i, j] = min(accumulated_cost[i-1, j-1], accumulated_cost[i-1, j], accumulated_cost[i, j-1]) + distances[i, j]


    # f3 = plt.figure(3)
    # distance_cost_plot(accumulated_cost, plt)

    path, cost = path_cost(x, y, accumulated_cost, distances)
    # print(path, end="\n")
    # print(cost)

    # f3 = plt.figure(3)
    # distance_cost_plot(accumulated_cost, plt)

    accumulated_cost = np.zeros((len(y), len(x)))
    accumulated_cost[0,0] = distances[0,0]
    for i in range(1, len(y)):
        accumulated_cost[i,0] = distances[i, 0] + accumulated_cost[i-1, 0]
    for i in range(1, len(x)):
        accumulated_cost[0,i] = distances[0,i] + accumulated_cost[0, i-1]
    for i in range(1, len(y)):
        for j in range(1, len(x)):
            accumulated_cost[i, j] = min(accumulated_cost[i-1, j-1], accumulated_cost[i-1, j], accumulated_cost[i, j-1]) + distances[i, j]
    plt.plot(x, 'b-', label='x')
    plt.plot(y, 'g-', label='y')
    plt.legend();
    paths = path_cost(x, y, accumulated_cost, distances)[0]

    if dtw_trace == 1:
        for [map_x, map_y] in paths: plt.plot([map_x, map_y], [x[map_x], y[map_y]], 'r')

    return cost
    # plt.show()