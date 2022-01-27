import read_data
import numpy as np
from random import randint

data = read_data.dictlist

file_no = randint(1, 100)

with open('generated' + str(file_no) + '.csv', 'w') as f:
    keys = list(data[0].keys())
    last_element = keys.pop()

    for key in keys:
        f.write(key)
        f.write(",")

    f.write(last_element + "\n")

    for state in data:
        f.write(state['State'] + ",")
        f.write(state['Population'] + ",")
        f.write(state['Seats'] + ",")

        a = np.random.random(6)
        a /= a.sum()  # make all the numbers sum to 1
        a *= round(int(state['Population']))  # make all the numbers sum to population
        a = a.astype(np.int64)  # convert the numbers from float64 to int64
        a = list(a)  # convert from numpy array to list

        last_number = a.pop()

        for rand_number in a:
            f.write(str(rand_number))
            f.write(",")

        f.write(str(last_number) + "\n")

