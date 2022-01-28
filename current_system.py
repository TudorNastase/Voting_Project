import read_data

data = read_data.dictlist

"""
Implementation of the current System for US elections. The winner on the given dataset should be Trump
"""


# computes the maximum value from the results dictionary and returns the key
# which is the candidate with the highest number of seats
def determine_winner(results):
    max_seats = max(results['Trump'], results['Bush'], results['Clinton'])
    for candidate in results.keys():
        if results[candidate] == max_seats:
            return candidate


# updates the results dictionary with the amount of seats that each candidate has won
# after this method is executed, the results dictionary will contain the final results of the election
def calculate_seats(results):
    for state in data:
        votes_trump = int(state['TCB']) + int(state['TBC'])
        votes_clinton = int(state['CTB']) + int(state['CBT'])
        votes_bush = int(state['BTC']) + int(state['BCT'])

        seats = int(state['Seats'])

        # gives the winner of this state's elections all the seats assigned to the state
        max_votes = max(votes_trump, votes_bush, votes_clinton)
        if votes_trump == max_votes:
            results['Trump'] += seats
        elif votes_bush == max_votes:
            results['Bush'] += seats
        elif votes_clinton == max_votes:
            results['Clinton'] += seats

#returns the winner of the election as a string
def main_program():
    # this dictionary is used to keep track of the overall results;
    # key is the candidate name, value is the number of seats they receive
    # each candidate starts with 0
    # will be updated by calculate_seats() method
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
