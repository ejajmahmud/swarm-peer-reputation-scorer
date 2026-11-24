"""Tests for ReputationScorer."""
import unittest
from swarm_peer_reputation_scorer.core import ReputationScorer

class TestReputationScorer(unittest.TestCase):
    def test_reputation_calculation(self):
        scorer = ReputationScorer(["good", "bad"])
        scorer.record_rating("eval", "good", 1.0)
        scorer.record_rating("eval", "bad", 0.0)

        scores = scorer.compute_scores()
        self.assertTrue(scores["good"] > scores["bad"])
        self.assertAlmostEqual(sum(scores.values()), 1.0, places=2)
