import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))
sys.path.insert(0, str(ROOT_DIR / "data" / "sales-analysis"))

from helpers import (
    apply_bulk_discount,
    apply_discount,
    calculate_compound_annual_growth_rate,
    calculate_profit_margin,
    calculate_return_on_investment,
    calculate_tax_and_grand_total,
    calculate_total,
    format_currency,
    summarize_sales_records,
)
from leetcode import (
    analyze_student_grades,
    cosine_similarity_1d,
    dot_product_1d,
    euclidean_distance_1d,
    filter_negative_numbers,
    find_largest_without_max,
    leaky_relu_1d,
    max_customer_wealth,
    mean_absolute_error,
    min_max_normalize,
    moving_average,
    multiply,
    relu_1d,
    root_mean_squared_error,
    running_sum_1d,
    sigmoid_1d,
    softmax_1d,
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


def test_softmax_mae_and_tax():
    probs = softmax_1d([1.0, 1.0, 1.0, 1.0])
    assert probs == [0.25, 0.25, 0.25, 0.25]
    assert mean_absolute_error([10.0, 20.0, 30.0], [12.0, 19.0, 27.0]) == 2.0

    tax_info = calculate_tax_and_grand_total(200.0, tax_rate_pct=18.0)
    assert tax_info["subtotal"] == 200.0
    assert tax_info["tax_amount"] == 36.0
    assert tax_info["grand_total"] == 236.0


def test_rmse_sigmoid_and_profit_margin():
    assert root_mean_squared_error([10.0, 20.0, 30.0], [10.0, 23.0, 34.0]) == 2.8868
    assert sigmoid_1d([0.0]) == [0.5]
    margin = calculate_profit_margin(500.0, 350.0)
    assert margin["net_profit"] == 150.0
    assert margin["margin_pct"] == 30.0


def test_relu_dot_product_and_roi():
    assert relu_1d([-3.5, 0.0, 2.25, -0.1, 7.0]) == [0.0, 0.0, 2.25, 0.0, 7.0]
    assert dot_product_1d([1.5, 2.0, 3.0], [4.0, 0.5, 2.0]) == 13.0
    roi = calculate_return_on_investment(1500.0, 1200.0)
    assert roi["net_return"] == 300.0
    assert roi["roi_pct"] == 25.0


def test_euclidean_distance_leaky_relu_and_cagr():
    assert euclidean_distance_1d([0.0, 0.0], [3.0, 4.0]) == 5.0
    assert leaky_relu_1d([-10.0, 0.0, 4.5], alpha=0.1) == [-1.0, 0.0, 4.5]
    assert calculate_compound_annual_growth_rate(1000.0, 1331.0, 3) == 10.0





