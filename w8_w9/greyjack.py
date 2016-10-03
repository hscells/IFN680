# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 09:46:28 2016

@author: frederic


Greyjack is a simplified version of Blackjack. 

The game is played with an infinite deck of cards (i.e. cards are sampled
with replacement)

Each draw from the deck results in a value between 1 and 10 (uniformly
distributed) with a colour of red (probability 1/3) or black (probability
2/3).

There are no aces or picture (face) cards in this game

At the start of the game both the player and the dealer draw one black
card (fully observed)

Each turn the player may either stick or hit.
If the player hits then she draws another card from the deck.
If the player sticks she receives no further cards.

The values of the player’s cards are added (black cards) or subtracted (red
cards)

If the player’s sum exceeds 21, or becomes less than 1, then she “goes
bust” and loses the game (reward -1)

If the player sticks then the dealer starts taking turns. The dealer always
sticks on any sum of 17 or greater, and hits otherwise. If the dealer goes
bust, then the player wins; otherwise, the outcome – win (reward +1),
lose (reward -1), or draw (reward 0) – is the player with the largest sum.


"""

import random
#    random.randint(a, b) return a random integer in range [a, b], 
#    including both end points


class State:
    '''
    Represent a state of greyjack game
    '''

    def __init__(self, dl_sum=0, pl_sum=0):
        '''
        player and dealer 
        '''
        self.pl_sum = pl_sum
        self.dl_sum = dl_sum
        self.reward = 0

        
    def do_first_round(self):
        '''
        First round: one black card each
        '''
        self.pl_sum = random.randint(1,10)
        self.dl_sum = random.randint(1,10)


    def went_bust(self):
        '''
        Test whether any player went bust and compute the reward of the game
        '''
        return (self.pl_sum<1 or self.pl_sum>21) or (self.dl_sum<1 or self.dl_sum>21)


    def compute_reward(self):
        '''
        Compute and return the reward of the game
        POST
           self.reward contains the reward for this game
        '''
        if self.pl_sum > 21 or self.pl_sum < 1:
            self.reward = -1
        elif self.dl_sum > 21 or self.dl_sum < 1:
            self.reward = 1
        elif self.pl_sum > self.dl_sum:
            self.reward = 1
        elif self.pl_sum < self.dl_sum:
            self.reward = -1
        else:
            self.reward = 0
        return self.reward
            

def step_greyjack(s, a):
    '''
    The function takes as input a state s (dealer’s first card 1–10 
    and the player’s sum 1–21), and an action a (hit or stick), and returns
    a pair   (next_state, is_game_over). 
    This function does not compute the reward.  To get the reward of a terminal
    state, call    State.compute_reward()
    PARAM
        s : State: current state.  s[0] dealer's first card, s[1] player's sum
        a : string: action ('hit' or 'stick')
    POST
        s is unchanged
    RETURN 
        next state, is_game_over
    '''

    a = a.lower()
    assert a=='hit' or a=='stick'

    ns = State(s.dl_sum, s.pl_sum)

    if a == 'hit':
        ns.pl_sum += draw_card()
        return ns, ns.went_bust()

    while not ns.went_bust():
        if ns.dl_sum < 17:
            ns.dl_sum += draw_card()
        else:
            break

    return ns, True


def draw_card():
    '''
    Draw a card, black with probability 2/3
    Return a positive integer for a black card, and  a negative
    integer for a red card
    '''
    if random.random() < 2.0/3:
        return random.randint(1,10)
    else:
        return -random.randint(1,10)

