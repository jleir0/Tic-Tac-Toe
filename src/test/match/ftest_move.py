import unittest
from src.microservices.match.services.match import MatchService 
from unittest.mock import MagicMock, patch

class TestMove(unittest.TestCase):

    def setUp(self):
        MatchService = MagicMock()
        MatchService.ocupiedSquares.return_value = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        MatchService.checkMove.return_value = True
        MatchService.newIterator.return_value = (1, 1)

    def test_move_successful(self):
        data = {
            'matchId': 'some_match_id',
            'playerId': 'X',
            'square': {'x': 2, 'y': 2}
        }

        response, status_code = MatchService.move(data)

        self.assertEqual(status_code, 200)
        self.assertEqual(response, "Congratulations, you won")

if __name__ == '__main__':
    unittest.main()
