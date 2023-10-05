import unittest
from src.microservices.match.services.match import MatchService 
from models import db, Match

class TestCreate(unittest.TestCase):

    def test_create_success(self):
        match_id = "test_match_id"
        expected_response = {
            "matchId": match_id
        }

        response, status_code = MatchService.create(match_id)
        self.assertEqual(status_code, 200)
        self.assertEqual(response, expected_response)

        match = Match.query.filter_by(matchId=match_id).first()
        self.assertIsNotNone(match)

    def test_create_failure(self):
        match_id = "error_match_id"
        
        with self.assertRaises(Exception):
            MatchService.create(match_id)
        match = Match.query.filter_by(matchId=match_id).first()
        self.assertIsNone(match)

if __name__ == '__main__':
    unittest.main()
