import read_data

data = read_data.dictlist

"""
Implements our own voting rule
It's a combination between plurality with run-off and proportional representation
For each state, the first two candidates receive a percentage of seats equal to the percentage of votes they got 
E.g.: if a candidate receives 40% of votes in a state they will receive 40% of the available seats for that state 
The losing candidate for each state redistributes their percentage of seats to the 2 other candidates, depending on the 
voter's second choice
E.g.: if Bush is eliminated in state 'X' and 20% voted for him in this state, we look at the second choice candidate for
the people that voted for him and redistribute their votes to the second choices
More about this can be found in the report 
"""


# return the candidate that will be eliminated for a given state
def round_one(state):
    # calculate number of votes for a single US state
    votes_trump = int(state['TCB']) + int(state['TBC'])
    votes_bush = int(state['BTC']) + int(state['BCT'])
    votes_clinton = int(state['CTB']) + int(state['CBT'])

    # return the candidate with the minimum number of votes
    min_votes = min(votes_trump, votes_bush, votes_clinton)
    if votes_trump == min_votes:
        return 'Trump'
    elif votes_bush == min_votes:
        return 'Bush'
    elif votes_clinton == min_votes:
        return 'Clinton'


# returns the votes for each state, after the votes for the eliminated candidate are excluded
def round_two(excl_cand, state):
    # base number of votes
    votes_trump = 0
    votes_bush = 0
    votes_clinton = 0

    if excl_cand == 'Trump':
        votes_clinton += int(state['CTB']) + int(state['CBT']) + int(state['TCB'])
        votes_bush += int(state['BTC']) + int(state['BCT']) + int(state['TBC'])
    elif excl_cand == 'Clinton':
        votes_trump += int(state['TCB']) + int(state['TBC']) + int(state['CTB'])
        votes_bush += int(state['BTC']) + int(state['BCT']) + int(state['CBT'])
    elif excl_cand == 'Bush':
        votes_trump += int(state['TCB']) + int(state['TBC']) + int(state['BTC'])
        votes_clinton += int(state['CTB']) + int(state['CBT']) + int(state['BCT'])

    return votes_trump, votes_bush, votes_clinton


def main_program():
    results = {
        'Trump': 0,
        'Bush': 0,
        'Clinton': 0
    }

    #for each state
    for state in data:
        excl_cand = round_one(state)
        votes_trump, votes_bush, votes_clinton = round_two(excl_cand, state)
        total_votes = votes_trump + votes_bush + votes_clinton

        total_seats = int(state['Seats'])

        # calculate what percentage of  seats each candidate receives and them to the results dictionary
        results['Trump'] += total_seats * (votes_trump/total_votes)
        results['Bush'] += total_seats * (votes_bush/total_votes)
        results['Clinton'] += total_seats * (votes_clinton/total_votes)

    # calculate winner of overall election
    max_seats = max(results['Trump'], results['Bush'], results['Clinton'])
    for candidate in results.keys():
        if results[candidate] == max_seats:
            return candidate, results


winner, results = main_program()
print("Results ", results)
print("Winner: ", winner)
