# helpers.py
from typing import Dict, List, Union


def calculate_total(quantity: Union[int, float], price: Union[int, float]) -> float:
    """Calculate total for a single item with non-negative input validation."""
    if quantity < 0 or price < 0:
        raise ValueError("quantity and price must be non-negative")
    return round(float(quantity * price), 2)


def format_currency(amount: Union[int, float]) -> str:
    """Format number as currency."""
    return f"${amount:,.2f}"


def summarize_sales_records(records: List[Dict[str, Union[int, float, str]]]) -> Dict[str, object]:
    """Aggregate grand total, total units, average order value, and top product by revenue."""
    if not records:
        return {
            "grand_total": 0.0,
            "total_units": 0,
            "average_order_value": 0.0,
            "top_product": None,
        }

    grand_total = 0.0
    total_units = 0
    best_product = None
    best_revenue = -1.0

    for row in records:
        qty = int(row.get("quantity", 0))
        price = float(row.get("price", 0.0))
        rev = calculate_total(qty, price)
        grand_total += rev
        total_units += qty
        if rev > best_revenue:
            best_revenue = rev
            best_product = str(row.get("product", ""))

    return {
        "grand_total": round(grand_total, 2),
        "total_units": total_units,
        "average_order_value": round(grand_total / len(records), 2),
        "top_product": best_product,
    }
