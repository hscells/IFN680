# -----Task 1 Description (party_animal.py)----------------------------#
#
#  The Bayesian network in Task 1 has the following variables:
#
#  P: a worker has attended a party
#  H: a worker has a headache
#  D: a worker is demotivated at work
#  U: a worker underperforms at work
#  A: a boss is angry
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
U = BayesNode('U', 'P D', {(T, T): 0.99, (T, F): 0.9, (F, T): 0.9, (F, F): 0.01})

party_animal = BayesNet([P.node_spec(), H.node_spec(), D.node_spec(), U.node_spec()])

A = BayesNode('A', 'U', {T: 0.95, F: 0.5})

party_animal.add(A.node_spec())

print(party_animal.variable_node('U'))
print(party_animal.variable_node('H').p(T, {'P': F}))
print(party_animal.variable_node('U').p(F, {'P': T, 'D': F}))
print(party_animal.variable_node('D').p(T, {}))


