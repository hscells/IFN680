
# -----Task 3 Description (wet_lawn.py)----------------------------#
#
#  One day morning Holmes wakes up to find his lawn wet. He wonders
#  if it has rained or if he left his sprinkler on. He looks at his
#  neighbour Watson's lawn and he sees it is wet too. So, he concludes
#  it must have rained. 
#
#  In the Bayesian network given in Figure 4 for Task 3, variables H, W,
#  R, and S are used to denote "Holmes lawn wet", "Watson lawn wet", "Rain"
#  and "Sprinkler", respectively. The probabilities in the network are
#  given below:
#  P(H=t|R=t,S=t)=1.0, P(H=t|R=t,S=f)=1.0, P(H=t|R=f,S=t)=0.9, P(H=t|R=f,S=f)=0.1
#  P(W=t|R=t)=1.0, P(W=t|R=f)=0.2, P(R=t)=0.2, P(S=t)=0.1
#   
#  Write code to compute P(H|R=f), and P(W|S=t, R=f) 
#  
# --------------------------------------------------------------------#
                       
# Code from AIMA including modules logic.py, utils.py, agents.py, and probability.py                        
from aima.probability import *
from aima.logic import *
from aima.utils import *

# WRITE YOUR SOLUTION HERE

# Define truth values
T, F = True, False

R = BayesNode('R', '', 0.2)
S = BayesNode('S', '', 0.1)
W = BayesNode('W', 'R', {T: 1.0, F: 0.2})
H = BayesNode('H', 'R S', {(T, T): 1.0, (T, F): 1.0, (F, T): 0.9, (F, F): 0.1})

wet_lawn = BayesNet([R.node_spec(), S.node_spec(), W.node_spec(), H.node_spec()])

print(enumeration_ask('H', {'R': F}, wet_lawn).show_approx())  # -> P(H|r)
print(enumeration_ask('W', {'S': T, 'R': F}, wet_lawn).show_approx())  # -> P(W|S=t, R=f)
