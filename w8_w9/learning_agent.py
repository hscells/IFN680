# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 16:57:33 2016

@author: frederic
"""

from __future__ import print_function
from __future__ import division

import numpy as np
import random

import greyjack


class RL_Agent:
    # Constructor, initialize attributes
    def __init__(self, gamma=0.9, n0=100):
        '''
        PARAM
          gamma : float : discount factor
          n0 : integer : parameter of the eps factor
        '''
        self.gamma = 0.9
        self.epsilon = 0.1
        self.n0 = n0

        # initialize tables for (state, action) pairs occurrences, values
        self.N = np.zeros((10, 21, 2))  # dl, pl, actions (hit, stick)
        self.Q = np.zeros((10, 21, 2))

        # action index dictionary
        self.translator = {'hit': 0, 'stick': 1, 0: 'hit', 1: 'stick'}

    def eps_greedy_choice(self, state):
        '''
        Return the eps greedy action ('hit' or 'stick')
        Epsilon dependent on number of visits to the state
        '''

        visits = sum(self.N[state.dl_sum - 1, state.pl_sum - 1, :])

        epsilon = self.n0 / (self.n0 + visits)

        if random.random() < epsilon:
            return 'hit' if random.random() < 0.5 else 'stick'

        return self.translator[np.argmax(self.Q[state.dl_sum - 1, state.pl_sum - 1, :])]

    def MC_learn(self, num_episodes=10000, episode_window=100, verbose=1):
        '''
        Play specified number of games, learning from experience using Monte-Carlo

        '''

        # Initialise
        game_outcomes = np.empty((num_episodes,))

        # Loop over episodes (complete game runs)
        for episode in range(num_episodes):

            episodes = []

            state = greyjack.State()
            state.do_first_round()

            game_over = False

            while not game_over:
                action = self.eps_greedy_choice(state)
                episodes.append((state, action))
                self.N[state.dl_sum - 1, state.pl_sum - 1, :] += 1
                state, game_over = greyjack.step_greyjack(state, action)

            game_outcomes[episode] = state.compute_reward()

            for state, action in episodes:
                learning_rate = 1.0 / (self.N[state.dl_sum - 1, state.pl_sum - 1, self.translator[action]])
                error = game_outcomes[episode] - self.Q[state.dl_sum - 1, state.pl_sum - 1, self.translator[action]]
                self.Q[state.dl_sum - 1, state.pl_sum - 1, self.translator[action]] += learning_rate * error

            if verbose > 0 and episode >= episode_window and episode % episode_window == 0:
                a, b = episode - episode_window, episode
                print('Mean game payoff between episodes {} and {} is {}'.format(a, b, game_outcomes[a:b].mean()))

        return game_outcomes

    def SARSA_learn(self, num_episodes=10000, episode_window=100, verbose=1):
        '''
        Play specified number of games, learning from experience using Temporal Difference
        '''
        # Initialise
        game_outcomes = np.empty((num_episodes,))

        # Loop over episodes (complete game runs)
        for episode in range(num_episodes):

            state = greyjack.State()
            state.do_first_round()
            action = self.eps_greedy_choice(state)

            game_over = False
            while not game_over:
                self.N[state.dl_sum - 1, state.pl_sum - 1, self.translator[action]] += 1

                n_state, game_over = greyjack.step_greyjack(state, action)

                learning_rate = 1.0 / self.N[state.dl_sum - 1, state.pl_sum - 1, self.translator[action]]

                if game_over:
                    reward = n_state.compute_reward()
                    game_outcomes[episode] = reward
                    delta = reward - self.Q[state.dl_sum - 1, state.pl_sum - 1, self.translator[action]]
                else:
                    n_action = self.eps_greedy_choice(n_state)
                    delta = self.gamma * self.Q[n_state.dl_sum - 1, n_state.pl_sum - 1, self.translator[n_action]] - self.Q[state.dl_sum - 1, state.pl_sum - 1, self.translator[action]]

                self.Q[state.dl_sum - 1, state.pl_sum - 1, self.translator[action]] += learning_rate * delta

                if not game_over:
                    state, action = n_state, n_action

            if verbose > 0 and episode >= episode_window and episode%episode_window == 0:
                a, b = episode-episode_window,episode
                print('Mean game payoff between episodes {} and {} is {}'.format(a, b, game_outcomes[a:b].mean()))

        return game_outcomes
