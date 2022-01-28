import read_data
data = read_data.dictlist

"""
Implements plurality with run-off for the overall US
The first round seeks to eliminate the candidate with the least amount of votes. 
In the second round, people that voted for the eliminated candidate will now vote for their second
favourite
The winner of the second round is the overall winner
For the given dataset the Winner is Bush
"""


# return the candidate with the lowest number of votes overall
def round_one():
    # dictionary used to store the results of the first round
    results = {
        'Trump': 0,
        'Bush': 0,
        'Clinton': 0
    }

    # calculate number of votes for overall US
    for state in data:
        votes_trump = int(state['TCB']) + int(state['TBC'])
        votes_bush = int(state['BTC']) + int(state['BCT'])
        votes_clinton = int(state['CTB']) + int(state['CBT'])

        results['Trump'] += votes_trump
        results['Bush'] += votes_bush
        results['Clinton'] += votes_clinton

    # return the candidate with the minimum number of votes
    min_votes = min(results['Trump'], results['Bush'], results['Clinton'])
    for candidate in results.keys():
        if results[candidate] == min_votes:
            return candidate


# returns the final election results and the winning candidate
def round_two(excl_cand):
    # dictionary used to store the results of the second round
    results = {
        'Trump': 0,
        'Bush': 0,
        'Clinton': 0
    }

    for state in data:
        # base number of votes
        votes_trump = 0
        votes_bush = 0
        votes_clinton = 0

        # calculate votes based on the excluded candidate
        # e.g: after Trump is eliminated his voters will vote for either Clinton or Bush, depending on who their
        # second favourite option is
        if excl_cand == 'Trump':
            votes_clinton += int(state['CTB']) + int(state['CBT']) + int(state['TCB'])
            votes_bush += int(state['BTC']) + int(state['BCT']) + int(state['TBC'])
        elif excl_cand == 'Clinton':
            votes_trump += int(state['TCB']) + int(state['TBC']) + int(state['CTB'])
            votes_bush += int(state['BTC']) + int(state['BCT']) + int(state['CBT'])
        elif excl_cand == 'Bush':
            votes_trump += int(state['TCB']) + int(state['TBC']) + int(state['BTC'])
            votes_clinton += int(state['CTB']) + int(state['CBT']) + int(state['BCT'])

        #update results
        results['Trump'] += votes_trump
        results['Bush'] += votes_bush
        results['Clinton'] += votes_clinton

    # return the candidate with the most votes(winner of the election overall)
    max_votes = max(results['Trump'], results['Bush'], results['Clinton'])
    for candidate in results.keys():
        if results[candidate] == max_votes:
            return candidate, results


excluded_candidate = round_one()
winner, results = round_two(excluded_candidate)
print("Excluded: ", excluded_candidate)
print("Results plurality with run off US: ", results)
print("Winner: ", winner)
