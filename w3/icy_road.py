
# -----Task 2 Description (icy_road.py)----------------------------#
#
#  Inspector Smith is waiting for Anderson and Young, who are driving
#  (separately) to meet him. It is winter. His secretary tells him that
#  Young has had an accident. He says, "It must be that the roads are icy.
#  I bet that Anderson will have an accident too.  I should go to lunch."
#  But his secretary says, "No, the roads are not icy, look at the window."
#  So, Smith says, "I guess I better wait for Anderson." 
#
#  In the Bayesian network given in Figure 3 for Task 2, variables  I, A, and Y
#  are used to denote "Icy", "Anderson crash" and "Young crash", respectively. 
#  The probabilities in the Bayesian network are:
#
#  P(I=t)=0.7, P(Y=t|I=t)=0.8, P(Y=t|I=f)=0.1
#  P(A=t|I=t)=0.8, P(A=t|I=f)=0.1
#
#  Write code to compute P(Y), P(I|Y=t), and P(A|Y=t) 
#  
# --------------------------------------------------------------------#
                       
# Code from AIMA including modules logic.py, utils.py, agents.py, and probability.py                        
from aima.probability import *
from aima.logic import *
from aima.utils import *

## WRITE YOUR SOLUTION HERE

# Define truth values
T, F = True, False

I = BayesNode('I', '', 0.7)
A = BayesNode('A', 'I', {T: 0.8, F: 0.1})
Y = BayesNode('Y', 'I', {T: 0.8, F: 0.1})

driving = BayesNet([I.node_spec(), A.node_spec(), Y.node_spec()])
print(enumeration_ask('Y', {}, driving).show_approx())  # -> P(Y)
print(enumeration_ask('I', {'Y': T}, driving).show_approx())  # -> P(I|y)
print(enumeration_ask('A', {'Y': T}, driving).show_approx())  # -> P(A|y)

