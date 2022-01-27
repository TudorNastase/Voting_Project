import read_data

data = read_data.dictlist

def determine_winner(results):
    max_votes = max(results['Trump'], results['Bush'], results['Clinton'])
    for candidate in results.keys():
        if results[candidate] == max_votes:
            return candidate


def calculate_votes(results):
    # calculate number of votes for overall US
    for state in data:
        votes_trump = int(state['TCB']) + int(state['TBC'])
        votes_bush = int(state['BTC']) + int(state['BCT'])
        votes_clinton = int(state['CTB']) + int(state['CBT'])

        results['Trump'] += votes_trump
        results['Bush'] += votes_bush
        results['Clinton'] += votes_clinton

def main_program():
    results = {
        'Trump': 0,
        'Bush': 0,
        'Clinton': 0
    }
    calculate_votes(results)
    winner = determine_winner(results)
    # print("Results plurality rule for overall US:")
    # print(results)
    # print("Winner is:", winner)
    return winner


main_program()