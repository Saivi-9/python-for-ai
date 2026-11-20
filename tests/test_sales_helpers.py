import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))
sys.path.insert(0, str(ROOT_DIR / "data" / "sales-analysis"))

from helpers import calculate_total, format_currency
from leetcode import (
    analyze_student_grades,
    filter_negative_numbers,
    find_largest_without_max,
    max_customer_wealth,
    multiply,
    running_sum_1d,
)


def test_calculate_total():
    assert calculate_total(3, 19.99) == 59.97
    assert calculate_total(0, 100.0) == 0.0


def test_format_currency():
    assert format_currency(1234.5) == "$1,234.50"
    assert format_currency(0) == "$0.00"


def test_leetcode_algorithms():
    assert running_sum_1d([1, 4, 6, 8, 11, 16]) == [1, 5, 11, 19, 30, 46]
    assert max_customer_wealth([[2, 8], [5, 5], [1, 20]]) == 21
    assert filter_negative_numbers([-3, 7, 0, 15, -8, 9, 2]) == [-3, -8]
    assert find_largest_without_max([12, 7, 25, 3, 18, 40, 9]) == 40
    assert multiply(6, 7) == 42

    grades = [
        [85, 90, 78],
        [60, 72, 68],
        [95, 88, 91],
        [70, 75, 80],
    ]
    summary = analyze_student_grades(grades)
    assert summary["totals"] == [253, 200, 274, 225]
    assert summary["best_student"] == 3
    assert summary["highest_total"] == 274
