"""CLI for Reputation Scorer."""
import argparse
from .core import ReputationScorer

def main():
    parser = argparse.ArgumentParser(description="Swarm Peer Reputation Scorer CLI")
    parser.add_argument("--demo", action="store_true", help="Run reputation scoring demo")
    args = parser.parse_args()

    scorer = ReputationScorer(["agent-1", "agent-2", "agent-3"])
    scorer.record_rating("supervisor", "agent-1", 0.95)
    scorer.record_rating("supervisor", "agent-2", 0.40)
    scorer.record_rating("supervisor", "agent-3", 0.85)

    scores = scorer.compute_scores()
    print("Computed Global Swarm Reputation Scores:", scores)

if __name__ == "__main__":
    main()
