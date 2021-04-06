#https://itu.kattis.com/sessions/skkmtp/problems/itu.disjointsets

from itu.algs4.fundamentals.uf import UF
from itu.algs4.stdlib.stdio import readInt, writeln
n=readInt()
m=readInt()
uf=UF(n)
for i in range(m):
    op=readInt()
    s=readInt()
    t=readInt()
    if op==0:
        print(int(uf.connected(s, t)))  
    if op==1:
        uf.union(s, t)