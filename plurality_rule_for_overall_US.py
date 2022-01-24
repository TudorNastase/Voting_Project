import read_data

data = read_data.dictlist

results = {
    'Trump': 0,
    'Bush': 0,
    'Clinton': 0
}


def determine_winner():
    max_votes = max(results['Trump'], results['Bush'], results['Clinton'])
    for candidate in results.keys():
        if results[candidate] == max_votes:
            return candidate


def calculate_votes():
    # calculate number of votes for overall US
    for state in data:
        votes_trump = int(state['TCB']) + int(state['TBC'])
        votes_bush = int(state['BTC']) + int(state['BCT'])
        votes_clinton = int(state['CTB']) + int(state['CBT'])

        results['Trump'] += votes_trump
        results['Bush'] += votes_bush
        results['Clinton'] += votes_clinton


calculate_votes()
winner = determine_winner()
print("Results plurality rule for overall US:")
print(results)
print("Winner is:", winner)
