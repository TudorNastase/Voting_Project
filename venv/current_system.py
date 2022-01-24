import read_data

data=read_data.dictlist

results={
    'Trump' : 0,
    'Bush'  : 0,
    'Clinton' : 0
}

def determine_winner():
    max_seats=max(results['Trump'],results['Bush'],results['Clinton'])
    for candidate in results.keys():
        if results[candidate] == max_seats:
            return candidate

def calculate_seats():
    for line in data:
        votes_trump=int(line['TCB'])+int(line['TBC'])
        votes_bush=int(line['BTC'])+int(line['BCT'])
        votes_clinton=int(line['CTB'])+int(line['CBT'])

        seats=int(line['Seats'])

        max_votes=max(votes_trump,votes_bush,votes_clinton)
        if votes_trump == max_votes:
            results['Trump']+=seats
        if votes_bush == max_votes:
            results['Bush']+=seats
        if votes_clinton == max_votes:
            results['Clinton']+=seats
calculate_seats()
winner=determine_winner()
print("Results:")
print(results)
print("Winner is:",winner)



