# Harry Scells Jul 2016
# IFN680 Advanced Topics in Artificial Intelligence
# Python 2.7

from aima.probability import ProbDist, JointProbDist

# -----------------

# We create a ProbDist object to represent the probability distribution for one random variable
Pr = ProbDist('Ct')
# The object represents the probability distribution of a person living in England, Scotland,
# or Wales
Pr['E'], Pr['S'], Pr['W'] = 0.88, 0.08, 0.04
print(Pr.show_approx())
print(Pr.prob['E'], Pr.prob['S'], Pr.prob['W'])

# -----------------

# Another way to create a ProbDist object is using counts. Assume there are 1000 people, 880
# live in England, 80 live in Scotland, and the rest (40) live in Wales
Pr = ProbDist('Ct', {'E': 880, 'S': 80, 'W': 40})
print(Pr.show_approx())
print(Pr.is_valid())  # The sum of the probabilities must be 1
Pr['E'], Pr['S'], Pr['W'] = 0.8, 0.08, 0.04
print(Pr.is_valid())  # Whoops! -> suddenly the probabilities do not sum to 1

# -----------------

# We can have an object to represent the probability distribution for a set of random variables
Pr = JointProbDist(['Mt', 'Ct'])
Pr['Eng', 'E'], Pr['Eng', 'S'], Pr['Eng', 'W'] = 0.836, 0.056, 0.024
Pr['Scot', 'E'], Pr['Scot', 'S'], Pr['Scot', 'W'] = 0.0352, 0.024, 0
Pr['Wel', 'E'], Pr['Wel', 'S'], Pr['Wel', 'W'] = 0.0088, 0, 0.016
print(Pr.show_approx())
print(Pr.values('Mt'))
