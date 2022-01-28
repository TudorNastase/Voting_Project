import read_data
import numpy as np

data = read_data.dictlist

"""
Following code creates 100 files with randomly generated votes, very similar to the given dataset
The data in the generated files is used to simulate results of elections. Conclusions drawn can be found in the report

Run this file before running plots.py 
"""

file_no = 0
while file_no!=100:
    #create file
    with open('generated' + str(file_no) + '.csv', 'w') as f:
        file_no+=1
        keys = list(data[0].keys())
        last_element = keys.pop()

        for key in keys:
            f.write(key)
            f.write(",")

        f.write(last_element + "\n")

        #generate the data per state
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

