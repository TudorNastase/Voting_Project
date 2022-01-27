import read_data

data = read_data.dictlist


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

    max_votes = max(votes_trump, votes_bush, votes_clinton)
    if votes_trump == max_votes:
        return 'Trump'
    elif votes_bush == max_votes:
        return 'Bush'
    elif votes_clinton == max_votes:
        return 'Clinton'


def main_program():
    results = {
        'Trump': 0,
        'Bush': 0,
        'Clinton': 0
    }

    for state in data:
        excl_cand = round_one(state)
        state_winner = round_two(excl_cand, state)

        seats = int(state['Seats'])

        results[state_winner] += seats

    max_seats = max(results['Trump'], results['Bush'], results['Clinton'])
    for candidate in results.keys():
        if results[candidate] == max_seats:
            return candidate, results


winner, results = main_program()
print("Results plurality rule with run off per state: ", results)
print("Winner: ", winner)
