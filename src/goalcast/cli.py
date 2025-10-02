"""
GoalCast Command Line Interface.

This module provides the main CLI entry point for the GoalCast prediction engine.
"""

import click
from rich.console import Console

from goalcast import __version__

console = Console()


@click.group()
@click.version_option(version=__version__, prog_name="goalcast")
def main() -> None:
    """GoalCast: EPL Prediction Engine with Advanced Statistical Modeling."""
    pass


@main.command()
def info() -> None:
    """Display information about GoalCast."""
    console.print(f"[bold cyan]GoalCast[/bold cyan] v{__version__}")
    console.print("\n[bold]EPL Prediction Engine[/bold]")
    console.print("Combining statistical rigor with LLM-powered insights\n")
    console.print("[dim]For more information, visit:[/dim]")
    console.print("[link]https://github.com/LinoGoncalves/GoalCast[/link]")


if __name__ == "__main__":
    main()
