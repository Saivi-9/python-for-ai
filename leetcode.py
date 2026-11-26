from typing import Dict, List
import math


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


def z_score_standardize(values: List[float]) -> List[float]:
    """Standardize numeric features to zero mean and unit population variance."""
    if not values:
        return []
    mean_val = sum(values) / len(values)
    variance = sum((v - mean_val) ** 2 for v in values) / len(values)
    std_val = math.sqrt(variance)
    if std_val == 0.0:
        return [0.0 for _ in values]
    return [round((v - mean_val) / std_val, 4) for v in values]


def cosine_similarity_1d(vec_a: List[float], vec_b: List[float]) -> float:
    """Compute cosine similarity between two equal-length 1D embedding vectors."""
    if len(vec_a) != len(vec_b) or not vec_a:
        raise ValueError("Vectors must be non-empty and of equal length")
    dot = sum(a * b for a, b in zip(vec_a, vec_b))
    norm_a = math.sqrt(sum(a * a for a in vec_a))
    norm_b = math.sqrt(sum(b * b for b in vec_b))
    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0
    return round(dot / (norm_a * norm_b), 4)


def moving_average(values: List[float], window: int) -> List[float]:
    """Compute simple sliding-window moving averages over a 1D numeric series."""
    if window <= 0:
        raise ValueError("window must be positive")
    if not values or window > len(values):
        return []
    out: List[float] = []
    window_sum = sum(values[:window])
    out.append(round(window_sum / window, 4))
    for i in range(window, len(values)):
        window_sum += values[i] - values[i - window]
        out.append(round(window_sum / window, 4))
    return out


def softmax_1d(logits: List[float]) -> List[float]:
    """Compute numerically stable softmax probabilities over a 1D logit vector."""
    if not logits:
        return []
    max_logit = max(logits)
    exps = [math.exp(x - max_logit) for x in logits]
    denom = sum(exps)
    return [round(v / denom, 4) for v in exps]


def mean_absolute_error(y_true: List[float], y_pred: List[float]) -> float:
    """Compute Mean Absolute Error (MAE) between two equal-length numeric prediction vectors."""
    if len(y_true) != len(y_pred) or not y_true:
        raise ValueError("y_true and y_pred must be non-empty and of equal length")
    total_err = sum(abs(t - p) for t, p in zip(y_true, y_pred))
    return round(total_err / len(y_true), 4)


def root_mean_squared_error(y_true: List[float], y_pred: List[float]) -> float:
    """Compute Root Mean Squared Error (RMSE) between two equal-length numeric vectors."""
    if len(y_true) != len(y_pred) or not y_true:
        raise ValueError("y_true and y_pred must be non-empty and of equal length")
    mse = sum((t - p) ** 2 for t, p in zip(y_true, y_pred)) / len(y_true)
    return round(math.sqrt(mse), 4)


def sigmoid_1d(values: List[float]) -> List[float]:
    """Apply the logistic sigmoid activation function 1 / (1 + exp(-x)) element-wise."""
    return [round(1.0 / (1.0 + math.exp(-x)), 4) for x in values]


def relu_1d(values: List[float]) -> List[float]:
    """Apply the Rectified Linear Unit (ReLU) activation max(0.0, x) element-wise."""
    return [round(max(0.0, float(x)), 4) for x in values]


def dot_product_1d(vec_a: List[float], vec_b: List[float]) -> float:
    """Compute the scalar dot product between two equal-length 1D vectors."""
    if len(vec_a) != len(vec_b) or not vec_a:
        raise ValueError("vec_a and vec_b must be non-empty and of equal length")
    return round(sum(float(a) * float(b) for a, b in zip(vec_a, vec_b)), 4)


def euclidean_distance_1d(vec_a: List[float], vec_b: List[float]) -> float:
    """Compute the L2 Euclidean distance between two equal-length 1D numeric vectors."""
    if len(vec_a) != len(vec_b) or not vec_a:
        raise ValueError("vec_a and vec_b must be non-empty and of equal length")
    sq_sum = sum((float(a) - float(b)) ** 2 for a, b in zip(vec_a, vec_b))
    return round(math.sqrt(sq_sum), 4)


def leaky_relu_1d(values: List[float], alpha: float = 0.01) -> List[float]:
    """Apply the Leaky ReLU activation function element-wise with negative slope alpha."""
    if alpha < 0.0:
        raise ValueError("alpha must be non-negative")
    return [round(float(x) if float(x) >= 0.0 else alpha * float(x), 4) for x in values]







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



