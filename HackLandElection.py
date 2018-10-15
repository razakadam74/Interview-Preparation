def electionWinner(votes):
    d = {}
    for vote in votes: 
        d[vote] = d.get(vote, 0) + 1
    w = max(d, key=d.get)
    highest_vote = d.get(w)
    posible_winners = [k for k,v in d.items() if float(v) >= highest_vote]
    posible_winners.sort()
    return posible_winners[-1]


# winner = electionWinner(['Alex','Michael','Harry','Dave','Michael', 'Victor', 'Harry', 'Alex', 'Mary', 'Mary'])
# print(winner)


def maxDifference(a):
    least = -1
    diff = -1
    if len(a) == 0: 
        return -1
    least = a[0]
    for i in range(1, len(a)):
        diff = max(diff, a[i] - least)
        least = min(least, a[i])
    return diff




print(maxDifference([7,9,5,6,3,2]))
