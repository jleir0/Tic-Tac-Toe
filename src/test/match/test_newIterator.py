import unittest
from src.microservices.match.services.match import MatchService 

class TestNewIterator(unittest.TestCase):

    def test_valid_moves(self):

        occupiedSquares = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]        

        moves = [
            ((1,0),(1,1)),
            ((1,2),(1,1)),
            ((2,1),(1,1)),
            ((0,1),(1,1))
        ]

        for move_direction, expected_result in moves:
            with self.subTest(move_direction=move_direction):
                result = MatchService.newIterator(occupiedSquares, move_direction[0], move_direction[1])
                self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
