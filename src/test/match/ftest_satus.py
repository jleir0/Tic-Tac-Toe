import unittest
from src.microservices.match.services.match import MatchService 

class TestStatus(unittest.TestCase):

    def test_status_match_found(self):
        match_id = 123
        expected_response = {
            "matchId": match_id,
            "status": "The match is playing",
            "next": "X",
            "overall": [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        }
        self.assertEqual(MatchService.status(match_id), (expected_response, 200))

    def test_status_match_not_found(self):
        match_id = 9999
        expected_response = ({"matchId": match_id, "status": "Match with id 9999 not found"}, 404)
        self.assertEqual(MatchService.status(match_id), expected_response)

if __name__ == '__main__':
    unittest.main()
