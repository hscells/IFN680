# -----Task 3 Description (node_sampling.py)----------------------------#
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
#  P(U=t|P=t, D=t)=0.999,  P(U=t|P=t, D=f)=0.9,  
#  P(U=t|P=f, D=t)=0.9, P(U=t|P=f, D=f)=0.01,  
#  
# --------------------------------------------------------------------#

# Code from AIMA including modules logic.py, utils.py, agents.py, and probability.py                        
from aima.probability import *
from aima.logic import *
from aima.utils import *

# WRITE YOUR SOLUTION HERE

# Define truth values
T, F = True, False

P = BayesNode('P', '', 0.2)
H = BayesNode('H', 'P', {T: 0.9, F: 0.2})
D = BayesNode('D', '', 0.4)
U = BayesNode('U', 'P D', {(T, T): 0.999, (T, F): 0.9, (F, T): 0.9, (F, F): 0.01})
A = BayesNode('A', 'U', {T: 0.95, F: 0.5})

party_animals = BayesNet(
    [P.node_spec(), H.node_spec(), D.node_spec(), U.node_spec(), A.node_spec()])


def node_sampling(X, event, bn, N):
    node = bn.variable_node(X)
    c = 0
    for i in xrange(N):
        if node.sample(event):
            c += 1.0
    return {True: c/N, False: (N-c)/N}

print(enumeration_ask('U', {'P': T, 'D': F}, party_animals).show_approx())
print

print(node_sampling('U', {'P': T, 'D': F}, party_animals, 1000))
print(node_sampling('U', {'P': T, 'D': F}, party_animals, 5000))
print(node_sampling('U', {'P': T, 'D': F}, party_animals, 20000))
