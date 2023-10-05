import unittest
from src.microservices.match.services.match import MatchService

class TestCheckMove(unittest.TestCase):
    
    def test_invalid_move_occupied_square(self):

        match = {
            "Xmoves": [[1, 0, 1], [0, 1, 0], [0, 0, 1]],
            "Omoves": [[0, 1, 0], [1, 0, 1], [1, 1, 0]]
        }        
        user = "Xmoves"
        x=2
        y=1

        expected_result = (400, 'You have introduced an invalid move.')

        self.assertEqual(MatchService.checkMove(match, user, x, y), expected_result)

    def test_invalid_move_already_marked(self):

        match = {
            "Xmoves": [[1, 0, 1], [0, 1, 0], [0, 0, 1]],
            "Omoves": [[0, 1, 0], [1, 0, 1], [1, 1, 0]]
        }        
        user = "Xmoves"
        x=2
        y=2

        expected_result = (400, 'You have introduced an invalid move.')

        self.assertEqual(MatchService.checkMove(match, user, x, y), expected_result)

    def test_valid_move(self):

        match = {
            "Xmoves": [[1, 0, 1], [0, 0, 0], [0, 0, 1]],
            "Omoves": [[0, 1, 0], [1, 0, 1], [1, 1, 0]]
        }        
        user = "Xmoves"
        x=1
        y=1

        expected_result = MatchService.checkMove(match, user, x, y)

        self.assertEqual(MatchService.checkMove(match, user, x, y), expected_result)

    def test_winning_move(self):
        
        match = {
            "Xmoves": [[1, 0, 0], [0, 1, 0], [0, 0, 0]],
            "Omoves": [[0, 1, 0], [1, 0, 0], [0, 0, 0]]
        }        
        user = "Xmoves"
        x=2
        y=2

        expected_result = MatchService.checkMove(match, user, x, y)

        self.assertEqual(MatchService.checkMove(match, user, x, y), expected_result)

if __name__ == '__main__':
    unittest.main()
