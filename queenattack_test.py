import unittest

from gurobi_queen_attack_k_solve import GurobiQueenAttackKSolve
from chess_board_drawing import ChessBoardDrawing

class GurobiQueenAttackKSolveTest(unittest.TestCase):
    def test_try(self, n = 5, k = 2):
        queenSolve = GurobiQueenAttackKSolve(n, k)
        sol = queenSolve.solve()
        #vẽ bàn cờ với chess_board_drawing.py
        chessBoardDrawing = ChessBoardDrawing(n, n,
                                 f'ChessBoard {n}x{n} with k = {k}.png')
        chessBoardDrawing.run(sol)
        #print constraint
        for c in queenSolve.model.getConstrs():
            print(c)
        return sol
    def test4_0(self):
        sol = self.test_try(4, 0)  
    def test8_1(self):
        sol = self.test_try(8, 1)
    def test8_2(self):
        sol = self.test_try(8,2)  
    

