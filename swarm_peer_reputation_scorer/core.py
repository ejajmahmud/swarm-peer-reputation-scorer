"""Core Reputation Scorer implementation."""
from typing import Dict, List, Tuple

class PeerRating:
    def __init__(self, rater_id: str, target_id: str, score: float):
        self.rater_id = rater_id
        self.target_id = target_id
        self.score = max(0.0, min(1.0, score))

class ReputationScorer:
    def __init__(self, peer_ids: List[str]):
        self.peer_ids = peer_ids
        self.ratings: List[PeerRating] = []

    def record_rating(self, rater: str, target: str, score: float):
        self.ratings.append(PeerRating(rater, target, score))

    def compute_scores(self) -> Dict[str, float]:
        if not self.peer_ids:
            return {}

        # Aggregate normalized scores
        scores = {p: 1.0 / len(self.peer_ids) for p in self.peer_ids}
        direct_sums: Dict[str, float] = {p: 0.0 for p in self.peer_ids}
        direct_counts: Dict[str, int] = {p: 0 for p in self.peer_ids}

        for r in self.ratings:
            if r.target_id in direct_sums:
                direct_sums[r.target_id] += r.score
                direct_counts[r.target_id] += 1

        for p in self.peer_ids:
            if direct_counts[p] > 0:
                scores[p] = direct_sums[p] / direct_counts[p]

        # Normalize to sum to 1.0
        total = sum(scores.values()) or 1.0
        return {p: round(s / total, 4) for p, s in scores.items()}
