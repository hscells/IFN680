import game, mcts, quantum_game

def experiment(n, p1, p2, p1name='p1', p2name='p2'):
    wins = {-1: 0, 1: 0}
    moves = {-1: {'len': 0, 'sum': 0}, 1: {'len': 0, 'sum': 0}}
    for i in range(1, n + 1):
        print('game {} of {}'.format(i, n))

        qg = quantum_game.Quantumgame()
        qg.randomize_board()

        p1.set_game(qg.clone())
        p2.set_game(qg.clone())

        p1.set_color(-1)
        p2.set_color(1)

        last_turn, legal_move_hist = game.play(qg, p1, p2, verbose=0)

        wins[-qg.turn] += 1
        moves[-1]['sum'] += sum(legal_move_hist[-1])
        moves[-1]['len'] += len(legal_move_hist[-1])
        moves[1]['sum'] += sum(legal_move_hist[1])
        moves[1]['len'] += len(legal_move_hist[1])

    print(moves[-1]['sum']/moves[-1]['len'])
    print(moves[1]['sum']/moves[1]['len'])
    print('wins: {}={}, {}={}'.format(p1name, wins[-1], p2name, wins[1]))


def random_mcts_game():
    p1 = game.Random_player(None)
    p2 = mcts.MCTS_player(None, iters=50)
    experiment(10, p1, p2, p1name='Random', p2name='MCTS')


def mcts_mcts_game():
    p1 = mcts.MCTS_player(None, iters=10)
    p2 = mcts.MCTS_player(None, iters=5)
    experiment(10, p1, p2, p1name='MCTS-1', p2name='MCTS-2')


if __name__ == '__main__':
    random_mcts_game()
    # mcts_mcts_game()
