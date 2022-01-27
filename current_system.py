import read_data

data = read_data.dictlist



def determine_winner(results):
    max_seats = max(results['Trump'], results['Bush'], results['Clinton'])
    for candidate in results.keys():
        if results[candidate] == max_seats:
            return candidate


def calculate_seats(results):
    for state in data:
        votes_trump = int(state['TCB']) + int(state['TBC'])
        votes_clinton = int(state['CTB']) + int(state['CBT'])
        votes_bush = int(state['BTC']) + int(state['BCT'])

        seats = int(state['Seats'])

        max_votes = max(votes_trump, votes_bush, votes_clinton)
        if votes_trump == max_votes:
            results['Trump'] += seats
        elif votes_bush == max_votes:
            results['Bush'] += seats
        elif votes_clinton == max_votes:
            results['Clinton'] += seats

def main_program():
    results = {
        'Trump': 0,
        'Bush': 0,
        'Clinton': 0
    }

    calculate_seats(results)
    winner = determine_winner(results)
    print("Results Current System:")
    print(results)
    print("Winner is:", winner)
    return winner
main_program()