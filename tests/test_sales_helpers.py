import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))
sys.path.insert(0, str(ROOT_DIR / "data" / "sales-analysis"))

from helpers import apply_bulk_discount, apply_discount, calculate_total, format_currency, summarize_sales_records
from leetcode import (
    analyze_student_grades,
    cosine_similarity_1d,
    filter_negative_numbers,
    find_largest_without_max,
    max_customer_wealth,
    min_max_normalize,
    moving_average,
    multiply,
    running_sum_1d,
    two_sum_indices,
    z_score_standardize,
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

    assert min_max_normalize([10.0, 20.0, 30.0]) == [0.0, 0.5, 1.0]
    assert min_max_normalize([5.0, 5.0]) == [0.0, 0.0]
    assert two_sum_indices([2, 7, 11, 15], 9) == [0, 1]


def test_summarize_sales_records():
    records = [
        {"product": "Laptop", "quantity": 2, "price": 1200.0},
        {"product": "Mouse", "quantity": 5, "price": 25.0},
    ]
    summary = summarize_sales_records(records)
    assert summary["grand_total"] == 2525.0
    assert summary["total_units"] == 7
    assert summary["average_order_value"] == 1262.5
    assert summary["top_product"] == "Laptop"
    assert apply_discount(200.0, 15.0) == 170.0
    assert z_score_standardize([10.0, 20.0, 30.0]) == [-1.2247, 0.0, 1.2247]
    assert cosine_similarity_1d([1.0, 0.0], [1.0, 0.0]) == 1.0
    assert cosine_similarity_1d([1.0, 0.0], [0.0, 1.0]) == 0.0

    assert apply_bulk_discount(200.0, quantity=12, threshold_qty=10, discount_pct=15.0) == 170.0
    assert apply_bulk_discount(200.0, quantity=5, threshold_qty=10, discount_pct=15.0) == 200.0


def test_z_score_and_moving_average():
    z = z_score_standardize([10.0, 20.0, 30.0])
    assert z == [-1.2247, 0.0, 1.2247]
    assert z_score_standardize([4.0, 4.0]) == [0.0, 0.0]
    assert moving_average([2.0, 4.0, 6.0, 8.0, 10.0], window=3) == [4.0, 6.0, 8.0]


