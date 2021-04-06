#https://itu.kattis.com/sessions/ke376g/problems/itu.balance

from itu.algs4.fundamentals.stack import Stack
from itu.algs4.stdlib.stdio import readLine

mystack = Stack()
mystr = readLine()
bal = True
for c in mystr:
    if c in ["(", "["]:
        mystack.push(c)
    if c in [")", "]"]:
        if mystack.is_empty():
            bal = False
            break
        lastone = mystack.pop()
        if c == ")" and lastone == "(":
            continue
        elif c == "]" and lastone == "[":
            continue
        else:
            bal = False
            break
            
bal = bal and mystack.is_empty()
print(int(bal))