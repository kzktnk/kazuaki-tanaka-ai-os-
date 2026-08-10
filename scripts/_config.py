"""Shared paths and labels for deliverable generation scripts."""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = REPO_ROOT / "outputs"

CLIENT_LABEL = "クライアント様"
CLIENT_SHORT = "クライアント"


def output_paths(filename: str) -> list[Path]:
    """Return output paths under repo outputs/ (directory created if needed)."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    return [OUTPUT_DIR / filename]
