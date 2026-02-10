from model import ProblemInstance, Event

import itertools

list = list(range(1, 10))
num = len(list)
combinations = []
for i in range(num+1):
    for subset in itertools.combinations(list, i):
        combinations.append(subset)


print(combinations)