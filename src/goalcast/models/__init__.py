"""
Statistical modeling module.

This module implements multiple statistical models for match outcome prediction:
- Poisson model (baseline)
- Dixon-Coles adjustment
- Bayesian hierarchical team strengths
- xG integration
- Copula-based joint score distributions
- In-play Markov chain models

Submodules:
    - poisson: Baseline Poisson model
    - dixon_coles: Dixon-Coles low-score adjustment
    - bayesian: Bayesian hierarchical modeling
    - xg: Expected goals integration
    - copula: Copula-based score distributions
    - markov: In-play Markov chain model
    - calibration: Model calibration and metrics
"""

__all__ = []
