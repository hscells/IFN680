# -----Task 1 Description (cookies.py)----------------------------#
#
#  Suppose there are two boxes of cookies. Box 1 contains 30 vanilla
#  cookies and 10 chocolate cookies. Box 2 contains 20 of each.
#  Write Python code calculate the following probabilities.
#
#  Question 1)
#  ---------- 
#  Let 'Box' be a random variable, its domain would be {'box1','box2'}.
#  Create an object of ProbDist to represent the probability distribution of 'Box'. 
#
#  Question 2)
#  ----------
#  Let 'Cookie' be a random variable, its domain would be {'vanilla', 'chocolate'}.
#  Create an object of JointProbDist to represent the joint probability distribution
#  of 'Box' and 'Cookie'. 
#
#  For this question, you need work out the joint probability for each event of
#  ('Box', 'Cookie'), and then assign these probabilities to the JointProbDict object.
#
#  Question 3)
#  ----------
#  If we randomly pick up a cookie from box 1, what is the probability that the 
#  cookie is vanilla? Similarly, if we randomly pick up a cookie from box 2, what
#  is the probability that the cookie is vanilla
#
#  This question is to calculate P(Cookie=chocolate|Box=box1) and P(Cookie=vanilla|Box=box2)
#
#  Question 4)
#  ----------
#  Suppose you choose one of the boxes at random and, without looking,
#  pick up a cookie at random. The cookie is vanilla. What is the probability
#  that it came from box1.
#
#  This question is to calculate P(Box=box1|Cookie=vanilla)
#
# --------------------------------------------------------------------#

# Code from AIMA including modules logic.py, utils.py, agents.py, and probability.py                        
from aima.probability import *
from aima.logic import *
from aima.utils import *

# WRITE YOUR SOLUTION HERE

# Answer 1
Box = ProbDist('Box')
Box['box1'], Box['box2'] = 0.5, 0.5

print(Box.show_approx())
print

# Answer 2
CookieBox = JointProbDist(['Box', 'Cookie'])
CookieBox['box1', 'vanilla'] = 0.375
CookieBox['box1', 'chocolate'] = 0.125
CookieBox['box2', 'vanilla'] = 0.25
CookieBox['box2', 'chocolate'] = 0.25

print(CookieBox.show_approx())
print

# Answer 3
Vanilla = enumerate_joint_ask('Cookie', {'Box': 'box1'}, CookieBox)
print(Vanilla['vanilla'])  # -> 0.75
Chocolate = enumerate_joint_ask('Cookie', {'Box': 'box2'}, CookieBox)
print(Chocolate['chocolate'])  # -> 0.5
print

# Answer 4
Box1Vanilla = enumerate_joint_ask('Box', {'Cookie': 'vanilla'}, CookieBox)
print(Box1Vanilla['box1'])  # -> 0.6
print

