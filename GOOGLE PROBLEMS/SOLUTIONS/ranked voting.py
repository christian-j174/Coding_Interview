"""
This is the problem that we used in the group mock interview session on Dec 12:

In a ranked-choice ballot, voters select up to five different candidates in order of preference. If at any given time,
a single candidate has more than 50% of the first-choice votes, that candidate is declared to be the winner. If not,
the candidate with the fewest votes is removed and the votes of
everyone who voted for that candidate are replaced with their next choice.
The process repeats until a winner is determined. Note that each voter is only ever voting for one candidate at a time.

Write a function called Election() which takes the name of a file as its only argument and
returns the name of the winner of an election whose votes are described in that file. Each line of
the file represents one voter and contains a comma-delimited list of names
representing the preferred voting order for that voter. Example:

Ms. First Choice, Mr. Second Choice
Stormageddon Dark Lord of All
Curly,Larry,Moe,Shemp,Stormageddon Dark Lord of All

"""


#The secret to solving this problem effectively is breaking it up into nice simple functions:

# Reads the file and returns the raw list of all votes.
def ReadVotes(path):
    out = []
    for line in open(path):
        out.append(line.rstrip().split(','))
    return out

# Counts the first vote on each line and returns a dict.
def CountVotes(votes):
    out = {}
    for vote in votes:
        name = vote[0]
        if name in out:
            out[name] += 1
        else:
            out[name] = 1
    return out

# Returns either the name of the winner or None.
def GetWinner(results):
    winner,count = None,0
    for key in results:
        val = results[key]
        if count < val:
            winner,count = key,val
    if count / len(results) > 0.5:
        return winner
    return None

# Returns the name of the biggest loser.
def GetLoser(results):
    loser,count = None,len(results)+1
    for key in results:
        val = results[key]
        if count > val:
            loser,count = key,val
    return loser

# Removes all votes for the loser.
def PurgeLoser(votes,loser):
    out = []
    for vote in votes:
        if loser in vote:
            del vote[loser]
        if len(vote) > 0:
            out.append(vote)
    return out

def Election(path):
    votes = ReadVotes(path)
    while True:
        results = CountVotes(votes)
        winner = GetWinner(results)
        if winner:
          return winner
        loser = GetLoser(results)
        votes = PurgeLoser(votes,loser)