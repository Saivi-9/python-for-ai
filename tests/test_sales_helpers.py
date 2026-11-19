import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "data" / "sales-analysis"))

from helpers import calculate_total, format_currency


def test_calculate_total():
    assert calculate_total(3, 19.99) == 59.97
    assert calculate_total(0, 100.0) == 0.0


def test_format_currency():
    assert format_currency(1234.5) == "$1,234.50"
    assert format_currency(0) == "$0.00"
