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

def calculate_votes():
    for line in data:
        votes_trump=int(line['TCB'])+int(line['TBC'])
        votes_bush=int(line['BTC'])+int(line['BCT'])
        votes_clinton=int(line['CTB'])+int(line['CBT'])

        results['Trump']+=votes_trump
        results['Bush']+=votes_bush
        results['Clinton']+=votes_clinton


calculate_votes()
winner=determine_winner()
print("Results:")
print(results)
print("Winner is:",winner)



