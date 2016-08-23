    
'''

Created on Sat 20 Aug 2016

@author: f.maire@qut.edu.au
    
    Test functions to illlustrate the classes of 
    packages 'game' and 'hexgame'
    
'''

import game, hexgame



def test_1():
    '''
       Game between two human players
    '''
    hg = hexgame.Hexgame(3)
    ph1 = game.Human_player(hg.clone())
    ph1.set_color(-1)
    ph2 = game.Human_player(hg.clone())    
    ph2.set_color(+1)
    hg.print_player_turn()
    game.play(hg, ph1, ph2, verbose = 1)


def test_2():
    '''
       Game between human player and minmax player
    '''
    hg = hexgame.Hexgame(5)
    ph1 = game.Human_player(hg.clone())
    ph1.set_color(-1)
    ph2 = game.Minmax_player(hg.clone(),hexgame.hexgame_eval)
    ph2.set_color(+1)

    game.play(hg, ph1, ph2, verbose = 1)

def test_3():
    '''
       debug Game between human player and minmax player
    '''
    hg = hexgame.Hexgame(3)
    hg.set_board([1,0,0,-1,1,-1,0,0,-1])
 
    ph1 = game.Human_player(hg.clone())
    ph1.set_color(-1)
    ph2 = game.Minmax_player(hg.clone(),hexgame.hexgame_eval)    
    ph2.set_color(+1)
    
  
    game.play(hg, ph1, ph2, verbose = 1)
    
if __name__ == "__main__":
   # test_1()
    test_2()
   # test_3()



# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + 
#                              CODE CEMETARY
# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + 

#
#    # Experiment 1:
#    # Player 1 and Player 2 are evenly matched with 3-ply deep search
#    # player 2 wins with a final score of 28
#    # player 1 0.2 s per ply player 2 0.4 s per ply
#    play(othello.game(), player(lambda x: minimax.minimax(x, 3)),
#         player(lambda x: minimax.minimax(x, 3)), False)
#    
#    # Experiment 2:
#    # now we show the significance of an evaluation function
#    # we weaken player1 to 2 ply deep but use the edge eval fun
#    # player 1 now beats player 2 with a score of 58!
#    # player 1 0.1 s per ply player 2 0.4 s per ply
#    play(othello.game(), player(lambda x: minimax.minimax(x, 2, othello.edge_eval)),
#         player(lambda x: minimax.minimax(x, 3)), False)
#
#    # Experiment 1 (with alpha-beta):
#    # player 1 0.1 s per ply, player 2 0.1 s per ply
#    play(othello.game(), player(lambda x: minimax.alphabeta(x, 3)),
#         player(lambda x: minimax.alphabeta(x, 3)), False)
#
#    # Experiment 2 (with alpha-beta):
#    # player 1 0.0 s per ply player 2 0.1 s per ply
#    play(othello.game(), player(lambda x: minimax.alphabeta(x, 2, othello.edge_eval)),
#         player(lambda x: minimax.alphabeta(x, 3)), False)
#

