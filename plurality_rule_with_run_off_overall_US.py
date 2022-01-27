import read_data
import matplotlib.pyplot as plt
data = read_data.dictlist

def round_one():
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


def round_two(excl_cand):
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

        if excl_cand == 'Trump':
            votes_clinton += int(state['CTB']) + int(state['CBT']) + int(state['TCB'])
            votes_bush += int(state['BTC']) + int(state['BCT']) + int(state['TBC'])
        elif excl_cand == 'Clinton':
            votes_trump += int(state['TCB']) + int(state['TBC']) + int(state['CTB'])
            votes_bush += int(state['BTC']) + int(state['BCT']) + int(state['CBT'])
        elif excl_cand == 'Bush':
            votes_trump += int(state['TCB']) + int(state['TBC']) + int(state['BTC'])
            votes_clinton += int(state['CTB']) + int(state['CBT']) + int(state['BCT'])

        results['Trump'] += votes_trump
        results['Bush'] += votes_bush
        results['Clinton'] += votes_clinton

    max_votes = max(results['Trump'], results['Bush'], results['Clinton'])
    for candidate in results.keys():
        if results[candidate] == max_votes:
            return candidate, results


excluded_candidate = round_one()
winner, results = round_two(excluded_candidate)
print("Excluded: ", excluded_candidate)
print("Results plurality with run off US: ", results)
print("Winner: ", winner)
