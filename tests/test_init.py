"""Test the main goalcast package."""

from goalcast import __author__, __email__, __version__


def test_version() -> None:
    """Test that version is defined."""
    assert __version__ == "0.1.0"


def test_author() -> None:
    """Test that author is defined."""
    assert isinstance(__author__, str)
    assert len(__author__) > 0


def test_email() -> None:
    """Test that email is defined."""
    assert isinstance(__email__, str)
    assert "@" in __email__ or __email__ == "your-email@example.com"
