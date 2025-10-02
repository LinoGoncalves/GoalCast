"""Test configuration and fixtures for GoalCast test suite."""

import pytest


@pytest.fixture
def sample_fixture_data() -> dict[str, str]:
    """Sample fixture data for testing."""
    return {
        "fixture_id": "epl_2025_gw01_001",
        "season": "2025-26",
        "round": "1",
        "home_team": "Arsenal",
        "away_team": "Chelsea",
    }
