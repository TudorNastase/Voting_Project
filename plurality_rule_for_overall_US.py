import read_data

data = read_data.dictlist

"""
This program calculates the results using the plurality rule for overall US
We just count up the votes for each candidate, regardless of the state it came from
The winner is teh candidate with the highest number of votes overall
The winner for the given dataset is Clinton
"""


# computes the maximum value from the results dictionary and returns the key
# which is the candidate with the highest number of votes
def determine_winner(results):
    max_votes = max(results['Trump'], results['Bush'], results['Clinton'])
    for candidate in results.keys():
        if results[candidate] == max_votes:
            return candidate


# iterates through every state, adds up all the votes for each candidate and stores the in the results dictionary
def calculate_votes(results):
    for state in data:
        votes_trump = int(state['TCB']) + int(state['TBC'])
        votes_bush = int(state['BTC']) + int(state['BCT'])
        votes_clinton = int(state['CTB']) + int(state['CBT'])

        results['Trump'] += votes_trump
        results['Bush'] += votes_bush
        results['Clinton'] += votes_clinton


# returns the winner of the election
def main_program():
    results = {
        'Trump': 0,
        'Bush': 0,
        'Clinton': 0
    }
    calculate_votes(results)
    winner = determine_winner(results)
    print("Results plurality rule for overall US:")
    print(results)
    print("Winner is:", winner)
    return winner


main_program()