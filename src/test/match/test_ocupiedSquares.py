import unittest
from src.microservices.match.services.match import MatchService 

class TestOccupiedSquares(unittest.TestCase):

    def test_occupied_squares(self):
        match = {
            "Xmoves": [[1, 0, 1], [0, 1, 0], [0, 0, 1]],
            "Omoves": [[0, 1, 0], [1, 0, 1], [1, 1, 0]]
        }

        expected_result = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

        self.assertEqual(MatchService.ocupiedSquares(match), expected_result)

    def test_invalid_move(self):
        match = {
            "Xmoves": [[1, 0, 1], [0, 1, 0], [0, 0, 1]],
            "Omoves": [[0, 1, 0], [1, 1, 1], [1, 1, 0]]
        }
        
        expected_result = (400, "You have introduced an invalid move.")

        self.assertEqual(MatchService.ocupiedSquares(match),expected_result)
            

if __name__ == '__main__':
    unittest.main()
