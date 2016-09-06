# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 14:15:30 2016

@author: f.maire@qut.edu.au

Implementation of a MCTS player

Last modified on 2016/09/04
 - Added more comments
 - Modify the code to reflect more the four basic steps  described in the lecture
    Selection, Expansion, Simulation, Backpropagation



We call 'mover' the player whose turn it is to move in the
present state of the board


"""

from __future__ import print_function
from __future__ import division

import random
import math

import game
#import quantum_game

class Node(object):
    '''
    Node class for building trees used in MCTS 
    '''
    C = 1.0 # constant of Bandit formula
            # See Node.value()

    def __init__(self, parent, state):
        '''
        Constructor for a node of a MCTS search tree
        parent: node of the previous board position
        state: current board position
        '''
        self.parent = parent
        self.state = state
        self.actions = self.state.legal_moves() # list of legal moves
        self.children = dict() # mapping action->state_node
        self.q = 0 # Estimate value of the state (estimate of game outcome +1 win -1 loss)
                   # The estimate is
        self.n = 0 # number of visits
        # initially, no action has been tried
        self.untried_actions = self.actions[:] # make a copy
        
    def value(self):
        '''
        Compute the UCB1 value
        '''
        if self.n ==0:
            return 0  #  uncertainty 
        return self.q + Node.C * math.sqrt(2*math.log(self.parent.n)/ self.n)
        
    def best_child(self):
        '''
        Return a pair best child node, and its corresponding move  
        Tie breaks randomly instead of first-wins as in built-in max()
        '''
        L = [   ( - child_node.value(), child_node, move ) 
                              for move, child_node in self.children.items() ]
        # Note the minus sign in front of child_node.value()
        # The value of a node is with respect to the mover (the player who has the turn)
                              
        max_v = -float('inf')  # max value known so far
        max_l = [] # list of pair (node,move) achieving the max value
        for cv, cn, cm in L: # child value, node, move
            if cv==max_v:
                max_l.append((cn,cm))
            elif cv>max_v:
                max_l = [(cn,cm)] # reset the list wrt this new max
                max_v = cv
        # pick one of the best moves randomly
        best_cn, best_cm = random.choice(max_l)  
        return best_cn, best_cm
                

class MCTS_player(game.Player):
    """
    This player performs a tree search using UCT. 
    See e.g. Browne et al. (2012) for a survey on monte carlo tree search
    """
    def __init__(self, game, iters=1500):
        self.iters = iters # number of iterations
        self.game = game

    def play(self, opp_move):
        '''
            Return a move to play using the UCT algorithm
            PARAMS
                opp_move: the last move played by the opponent
            RETURN
                a move
            PRE:
                Game state not terminal                 
        ''' 
        # Maintain own copy of the board               
        if opp_move is not None:
            self.game.do_move(opp_move)
        # create a search tree rooted at current position
        root = Node(None,self.game.clone())
        for _ in range(self.iters):
            # -- Selection step --
            node = self.tree_policy(root)  # tree policy
            # -- Expansion step --            
            if not node.state.is_terminal():
                node = self.expand(node)            
            # -- Simulation step --                
            node.reward = self.roll_out(node) # result of a playout
            # -- Backpropagation step --
            self.back_up(node) # backpropagate the outcome up to the root
        #
        # pick a best move at the root node
        _, move = root.best_child()
        # maintain own copy of the board
        self.game.do_move(move)
        return move

    def tree_policy(self, node):
        '''
        Go down the tree to select a node to expand.
        Return the node that should be expanded or is terminal
        '''
        # Descend to best child, unless leaf node.
        while not node.state.is_terminal():
            if node.untried_actions:
                break # self.expand(node)
            else:
                node, _ = node.best_child() # ignore the move returned 
        return node # terminal or can be expanded

    def expand(self, node):
        '''
        Pick an untried action from current node
        create a new chid node and return this child    
        PRE
           Some actions haven't been tried yet
        '''
        action = random.choice(node.untried_actions)
        node.untried_actions.remove(action)
        child_state = node.state.clone()
        child_state.do_move(action)
        child_node = Node(node, child_state)
        node.children[action] = child_node
        return child_node

    def roll_out(self, node):
        '''
        Return the payoff of the game for the mover
        -1 loss
        +1 win
        '''
        roll_out_state = node.state.clone()
        while not roll_out_state.is_terminal():    
            move = random.choice(roll_out_state.legal_moves())
            roll_out_state.do_move(move)    
        return -1 if node.state.turn == roll_out_state.turn else +1

    def back_up(self, node):
        '''
        Backup the outcome of the playout up to the root node
        '''
        r = node.reward # -1 loss  ,   +1 win
        while node is not None:
            node.n += 1
            node.q = ((node.n - 1)/node.n) * node.q + 1/node.n * r
            node = node.parent
            r = -r


# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + 
#                              CODE CEMETARY
# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + 


#        L = [ (child_node.value(),child_node,move) 
#                              for move, child_node in self.children.items() ]
#        # 
#        max_v = -float('inf')  # max value known so far
#        max_l = [] # list of pair (node,move) achieving max value
#        for cv, cn, cm in L:
#            if cv==max_v:
#                max_l.append((cn,cm))
#            elif cv>max_v:
#                max_l = [(cn,cm)] # reset the list for this new max
#                max_v = cv
#        # pick one of the best moves randomly
#        best_cn, best_cm = random.choice(max_l)  
#        return best_cn, best_cm
