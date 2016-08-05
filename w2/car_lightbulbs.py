# -----Task 3 Description (car_lightbulbs.py)---------------------------- #
#
#  You are given the following assumptions for a car:
#    The car has N light bulbs.
#    Each light bulb has two states, working or not working.  
#    The prior probability that each light bulb is not working is 0.12.
#    All light bulbs are independent with each other
#
#  1) Create a object of JointProbDist to represent the joint probability 
#     distribution of the 3 Boolean variables, calculate the probability
#     for each event of the 3 variables, and assign the probabilities to
#     the JointProbDist object.
#
#  2) Repeat the first question assuming that the number of light bulbs is
#     N which is a variable. 
#     
# -------------------------------------------------------------------- #

# Code from AIMA including modules logic.py, utils.py, agents.py, and probability.py                        
from aima.probability import *
from aima.logic import *
from aima.utils import *

# WRITE YOUR SOLUTION HERE

T, F = True, False

# 1)
# Create an object of JointProbDist to represent the joint probability distribution of 3
#  variables
# Assign each event with a probability 
# Check whether the probability distribution is valid or not
Bulbs = JointProbDist(['Bulb1', 'Bulb2', 'Bulb3'],
                      {'Bulb1': [T, F], 'Bulb2': [T, F], 'Bulb3': [T, F]})
prob_false = 0.12
prob_true = 1 - 0.12

Bulbs[F, T, T] = pow(prob_true, 2) * prob_false
Bulbs[T, F, T] = pow(prob_true, 2) * prob_false
Bulbs[T, T, F] = pow(prob_true, 2) * prob_false

Bulbs[F, F, T] = pow(prob_false, 2) * prob_true
Bulbs[F, T, F] = pow(prob_false, 2) * prob_true
Bulbs[T, F, F] = pow(prob_false, 2) * prob_true

Bulbs[F, F, F] = pow(prob_false, 3)

Bulbs[T, T, T] = pow(prob_true, 3)

print(Bulbs.show_approx())
print(Bulbs.is_valid())
print

# 2)
# a)Generate N variables

n_bulbs = 8
bulb_names = []
bulb_values = {}

for i in xrange(n_bulbs):
    bulb_names.append('Bulb' + str(i + 1))
    bulb_values[bulb_names[i]] = [True, False]

# b)Each variable has two values, true or false, create a dict to specify the values for each
#  variable
#   Create an object of JointProbDist to represent the joint probability distribution for the
#  N variables
NBulbs = JointProbDist(bulb_names, bulb_values)

# c)Generate all events
#   Assign a probability to each of the events
#   Check whether the probability distribution is valid or not
events = all_events_jpd(bulb_names, NBulbs, {'Bulb1': T})
for event in events:
    prob = 1
    for (key, val) in event.items():
        if val == F:
            prob *= prob_false
        else:
            prob *= prob_true
    NBulbs[event] = prob

# print(NBulbs.show_approx())
print(NBulbs.is_valid())

# d) Calculate the probability of each variable b, i.e., p(b)
for bulb in bulb_names:
    prob = enumerate_joint_ask(bulb, {}, NBulbs)
    print(bulb, prob.show_approx())
print

# e) Calculate p(B3|B1=false, B2=true), you can choose three different variables
print(enumerate_joint_ask(bulb_names[0], {bulb_names[1]: F, bulb_names[2]: T}, NBulbs)
      .show_approx())
