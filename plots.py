import csv
import matplotlib.pyplot as plt
import own_rule
import plurality_rule_for_overall_US as pl_US
import current_system as cur_sis

"""
program that creates plot from the generated data
run generate_data.py  before running this 
Explanation and significance of plots in the report
"""

arr = [0, 0, 0]
arr1= [0, 0, 0]
arr2= [0, 0, 0]
candidates = ['Trump', 'Bush', 'Clinton']
ct=0
ct1=0
ct2=0
for i in range(100):
    dictlist = []
    filename='generated' + str(i) +'.csv'

    with open(filename, mode='r') as inp:
        reader = csv.DictReader(inp)
        for row in reader:
            dictlist.append(row)
        own_rule.data=dictlist
        winner=own_rule.main_program()[0]
        if winner == 'Trump':
            arr[0]+=1
        if winner == 'Clinton':
            arr[1]+=1
        if winner == 'Bush':
            arr[2]+=1


        pl_US.data=dictlist
        winner1=pl_US.main_program()
        if winner1 == 'Trump':
            arr1[0]+=1
        if winner1 == 'Clinton':
            arr1[1]+=1
        if winner1 == 'Bush':
            arr1[2]+=1



        cur_sis.data=dictlist
        winner2 = cur_sis.main_program()
        if winner2 == 'Trump':
            arr2[0]+=1
        if winner2 == 'Clinton':
            arr2[1]+=1
        if winner2 == 'Bush':
            arr2[2]+=1

        if winner == winner1:
            ct+=1
        if winner == winner2:
            ct1+=1
        if winner1 == winner2 == winner:
            ct2+=1


plt.bar(candidates, arr, color='g')
plt.show()
plt.bar(candidates, arr1, color='r')
plt.show()
plt.bar(candidates, arr2, color='b')
plt.show()
print('winner of own rule same as plurality:',ct)
print( 'winner of own rule same as current system',ct1)
print(ct2)

