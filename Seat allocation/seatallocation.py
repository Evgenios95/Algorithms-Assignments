#https://itu.kattis.com/sessions/iu6uso/problems/itu.seatallocation

from itu.algs4.sorting.max_pq import MaxPQ
from itu.algs4.stdlib.stdio import readInt

n=readInt()
m=readInt()
votes=[readInt() for i in range(n)]

class PolPart:
    def __init__(self, votes):
        self.votes=votes
        self.seats=0
        self.hondt=self.votes/(self.seats+1)
        
    def add_s(self):
        self.seats+=1
        self.hondt=self.votes/(self.seats+1)
        
    def __lt__(self, other):
        return self.hondt < other.hondt
    
maxPrioQ=MaxPQ()
list_of_parties =list()

for i in range(n):
    p = PolPart(votes[i])
    maxPrioQ.insert(p)
    list_of_parties.append(p)
    
for _ in range(m):
    highest = maxPrioQ.del_max()
    highest.add_s()
    maxPrioQ.insert(highest)
    
for party in list_of_parties:
    print(party.seats)