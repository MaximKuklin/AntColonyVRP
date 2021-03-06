import numpy as np
from os.path import join
import os
from algorithms.ant_colony import VPR
from tools.data_loader import get_data

files_A = os.listdir('./data/benchmark/A')
files_A.sort()
files_B = os.listdir('./data/benchmark/B')
files_B.sort()

cases = []
for file in files_A:
    case = get_data('A/' + file)
    if case:
        cases.append(case)
for file in files_B:
    case = get_data('B/' + file)
    if case:
        cases.append(case)

i = 11
for i in range(len(cases)):
    print(cases[i]['name'])
    test = VPR(cases[i]['n_trucks'], cases[i]['dimension'], cases[i]['capacity'], cases[i]['demands'], cases[i]['adj_matrix'])
    test.compute()
    print()