# -----Task 2 Description (Tasmania_weather.py)---------------------------- #
#
#  The weather in Tasmania can be summarized as: if it rains one day there
#  is a 70% chance it will rain the following day; if it is sunny one day
#  there is 40% chance it will be sunny the following day. You can assume
#  there are two random variables for this task, which are Today and Yesterday.
#  The two variables have the same value domain which is {'sunny', 'raining'}.
#
#  1)
#  Assuming that the probability it rained yesterday is 0.5, create an object
#  of JointProbDist to represent the joint probability distribution of the weather
#  for two days, Today and Yesterday, i.e., to calculate the following joint
#  probabilities:
#  
#  P(Today=raining, Yesterday=raining)
#  P(Today=sunny, Yesterday=raining) 
#  P(Today=raining, Yesterday=sunny)
#  P(Today=sunny, Yesterday=sunny)
#
#  2)
#  Assuming that P is the joint probability distribution for two random
#  variables X and Y. Write a function to calculate the conditional 
#  probability of X with value X_value given Y with value Y_value, i.e.,
#               P(X=X_value | Y=Y_value)
#
#  The function has four parameters, the signature of the function is:
#
#      conditional_probability(X, X_value, given_Y, Y_value, P)
#
#  Then, using the function to compute the probability it was raining yesterday given
#  that it is sunny today, i.e., P(Yesterday=raining|Today=sunny). 
#
#  Similarly, using the function to compute the probability it was sunny yesterday
#  given that it is raining today, i.e., P(Yesterday=sunny|Today=raining).
#
# -------------------------------------------------------------------- #

# Code from AIMA including modules logic.py, utils.py, agents.py, and probability.py                        
from aima.probability import *
from aima.logic import *
from aima.utils import *

# WRITE YOUR SOLUTION HERE

# Answer 1

#  C(Today=raining, Yesterday=raining) -> 0.7
#  C(Today=sunny, Yesterday=raining)  -> 0.3
#  C(Today=raining, Yesterday=sunny) -> 0.6
#  C(Today=sunny, Yesterday=sunny) -> 0.4

Weather = JointProbDist(['Today', 'Yesterday'])
Weather['raining', 'raining'] = 0.35
Weather['sunny', 'raining'] = 0.15
Weather['raining', 'sunny'] = 0.3
Weather['sunny', 'sunny'] = 0.2

print(Weather.is_valid())
print


# Answer 2


def conditional_probability(X, X_val, Y, Y_val, P):
    evidence = {Y: Y_val}
    prob_x = enumerate_joint_ask(X, evidence, P)
    return prob_x[X_val]


print(conditional_probability('Yesterday', 'raining', 'Today', 'sunny', Weather))  # -> 0.428571
print(conditional_probability('Yesterday', 'sunny', 'Today', 'raining', Weather))  # -> 0.461538
