# -----Task 2 Description (approx_joint_probability.py)----------------------------#
#
#  The Bayesian network in Task 1 has the following variables:
#
#  P: the worker has attended a party
#  H: the worker has a headache
#  D: the worker is demotivated at work
#  U: the worker underperforms at work
#  A: the boss is angry
#
#  The probabilities in the Bayesian network are given below:
#
#  P(P=t)=0.2, P(D=t)=0.4, P(H=t|P=t)=0.9, P(H=t|P=f)=0.2
#  P(U=t|P=t, D=t)=0.999,  P(U=t|P=t, D=f)=0.9  
#  P(U=t|P=f, D=t)=0.9, P(U=t|P=f, D=f)=0.01
# 
# --------------------------------------------------------------------##

# Code from AIMA including modules logic.py, utils.py, agents.py, and probability.py                        
from aima.probability import *
from aima.logic import *
from aima.utils import *

# WRITE YOUR SOLUTION HERE

# create a Bayesian network
T, F = True, False

P = BayesNode('P', '', 0.2)
H = BayesNode('H', 'P', {T: 0.9, F: 0.2})
D = BayesNode('D', '', 0.4)
U = BayesNode('U', 'P D', {(T, T): 0.999, (T, F): 0.9, (F, T): 0.9, (F, F): 0.01})
A = BayesNode('A', 'U', {T: 0.95, F: 0.5})

party_animals = BayesNet(
    [P.node_spec(), H.node_spec(), D.node_spec(), U.node_spec(), A.node_spec()])

# Q1

At = enumeration_ask('A', {'U': T}, party_animals)[T]
Ut = enumeration_ask('U', {'P': T, 'D': F}, party_animals)[T]
Ht = enumeration_ask('H', {'P': T}, party_animals)[T]
Pt = enumeration_ask('P', {}, party_animals)[T]
Df = enumeration_ask('D', {}, party_animals)[F]

print(At, Ut, Ht, Pt, Df)

print(At * Ut * Ht * Pt * Df)


# Q2

def joint_probability(e, bn, N):
    c = 0
    for i in xrange(N):
        if consistent_with(e, prior_sample(bn)):
            c += 1
    return (c * 1.0) / N

print(joint_probability({'A': T, 'U': T, 'H': T, 'P': T, 'D': F}, party_animals, 1000))
print(joint_probability({'A': T, 'U': T, 'H': T, 'P': T, 'D': F}, party_animals, 2000))
print(joint_probability({'A': T, 'U': T, 'H': T, 'P': T, 'D': F}, party_animals, 5000))
