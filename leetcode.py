from typing import Dict, List


def running_sum_1d(nums: List[int]) -> List[int]:
    """Compute the cumulative 1D running sum of an integer array."""
    result: List[int] = []
    acc = 0
    for val in nums:
        acc += val
        result.append(acc)
    return result


def max_customer_wealth(accounts: List[List[int]]) -> int:
    """Return the maximum wealth across all customer bank accounts."""
    if not accounts:
        return 0
    return max(sum(account) for account in accounts)


def filter_negative_numbers(numbers: List[int]) -> List[int]:
    """Return all strictly negative numbers in the input list."""
    return [num for num in numbers if num < 0]


def find_largest_without_max(nums: List[int]) -> int:
    """Find the largest integer in a non-empty list without calling built-in max()."""
    if not nums:
        raise ValueError("nums must not be empty")
    largest = nums[0]
    for item in nums:
        if item > largest:
            largest = item
    return largest


def analyze_student_grades(grades: List[List[int]]) -> Dict[str, object]:
    """Calculate per-student totals and identify the 1-indexed top student without built-in max()."""
    if not grades:
        raise ValueError("grades must not be empty")

    grade_totals: List[int] = []
    for student_scores in grades:
        student_sum = 0
        for score in student_scores:
            student_sum += score
        grade_totals.append(student_sum)

    highest_total = grade_totals[0]
    for total in grade_totals:
        if highest_total < total:
            highest_total = total

    best_student = grade_totals.index(highest_total) + 1
    return {
        "totals": grade_totals,
        "best_student": best_student,
        "highest_total": highest_total,
    }


def greet(name: str) -> str:
    msg = f"Hello! {name}"
    print(msg)
    return msg


def multiply(a: int, b: int) -> int:
    product = a * b
    print(f"The product of {a} and {b} is {product}")
    return product


def min_max_normalize(values: List[float]) -> List[float]:
    """Scale numeric feature values into the [0.0, 1.0] range for AI/ML preprocessing."""
    if not values:
        return []
    lo = min(values)
    hi = max(values)
    if hi == lo:
        return [0.0 for _ in values]
    span = hi - lo
    return [round((v - lo) / span, 4) for v in values]


def two_sum_indices(nums: List[int], target: int) -> List[int]:
    """Return 0-based indices of two numbers in nums that add up to target in O(n) time."""
    seen: Dict[int, int] = {}
    for idx, val in enumerate(nums):
        complement = target - val
        if complement in seen:
            return [seen[complement], idx]
        seen[val] = idx
    return []



if __name__ == "__main__":
    nums = [1, 4, 6, 8, 11, 16]
    print(sum(nums))
    print(running_sum_1d(nums))

    accounts = [[2, 8], [5, 5], [1, 20]]
    accounts_total = [sum(acc) for acc in accounts]
    print(accounts_total)
    print("Max customer wealth:", max_customer_wealth(accounts))

    numbers = [-3, 7, 0, 15, -8, 9, 2]
    less_than_zero = filter_negative_numbers(numbers)
    print(len(less_than_zero))
    print(less_than_zero)

    num = [12, 7, 25, 3, 18, 40, 9]
    print(find_largest_without_max(num))

    grades = [
        [85, 90, 78],
        [60, 72, 68],
        [95, 88, 91],
        [70, 75, 80],
    ]
    summary = analyze_student_grades(grades)
    print(summary["totals"])
    for idx, total in enumerate(summary["totals"], start=1):
        print(f"Student {idx} Total: {total}")
    print(f"Best Student: Student {summary['best_student']}")
    print(f"Highest Total: {summary['highest_total']}")



