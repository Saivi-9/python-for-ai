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


def apply_discount(amount: Union[int, float], discount_pct: float) -> float:
    """Apply a percentage discount in [0.0, 100.0] to a non-negative amount."""
    if amount < 0:
        raise ValueError("amount must be non-negative")
    if discount_pct < 0.0 or discount_pct > 100.0:
        raise ValueError("discount_pct must be between 0.0 and 100.0")
    return round(float(amount) * (1.0 - discount_pct / 100.0), 2)



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


def apply_bulk_discount(
    total: Union[int, float],
    quantity: int,
    threshold_qty: int = 10,
    discount_pct: float = 10.0,
) -> float:
    """Apply a percentage discount when order quantity meets or exceeds threshold_qty."""
    if total < 0 or quantity < 0:
        raise ValueError("total and quantity must be non-negative")
    if not (0.0 <= discount_pct <= 100.0):
        raise ValueError("discount_pct must be between 0 and 100")
    if quantity >= threshold_qty:
        return round(float(total) * (1.0 - discount_pct / 100.0), 2)
    return round(float(total), 2)


def calculate_tax_and_grand_total(
    subtotal: Union[int, float],
    tax_rate_pct: float = 18.0,
) -> Dict[str, float]:
    """Compute sales tax amount and grand total for a non-negative subtotal and tax rate percentage."""
    if subtotal < 0:
        raise ValueError("subtotal must be non-negative")
    if tax_rate_pct < 0.0 or tax_rate_pct > 100.0:
        raise ValueError("tax_rate_pct must be between 0.0 and 100.0")
    sub = round(float(subtotal), 2)
    tax = round(sub * (tax_rate_pct / 100.0), 2)
    return {
        "subtotal": sub,
        "tax_amount": tax,
        "grand_total": round(sub + tax, 2),
    }


def calculate_profit_margin(
    revenue: Union[int, float],
    cost: Union[int, float],
) -> Dict[str, float]:
    """Compute net profit and gross profit margin percentage for non-negative revenue and cost."""
    if revenue < 0 or cost < 0:
        raise ValueError("revenue and cost must be non-negative")
    rev = round(float(revenue), 2)
    cst = round(float(cost), 2)
    net_profit = round(rev - cst, 2)
    margin_pct = round((net_profit / rev) * 100.0, 2) if rev > 0 else 0.0
    return {
        "revenue": rev,
        "cost": cst,
        "net_profit": net_profit,
        "margin_pct": margin_pct,
    }


def calculate_return_on_investment(
    gain_from_investment: Union[int, float],
    cost_of_investment: Union[int, float],
) -> Dict[str, float]:
    """Compute net return and Return on Investment (ROI) percentage for a positive investment cost."""
    if cost_of_investment <= 0:
        raise ValueError("cost_of_investment must be positive")
    if gain_from_investment < 0:
        raise ValueError("gain_from_investment must be non-negative")
    gain = round(float(gain_from_investment), 2)
    cost = round(float(cost_of_investment), 2)
    net_return = round(gain - cost, 2)
    roi_pct = round((net_return / cost) * 100.0, 2)
    return {
        "gain": gain,
        "cost": cost,
        "net_return": net_return,
        "roi_pct": roi_pct,
    }


def calculate_compound_annual_growth_rate(
    beginning_value: Union[int, float],
    ending_value: Union[int, float],
    years: Union[int, float],
) -> float:
    """Compute Compound Annual Growth Rate (CAGR) as a percentage over a positive number of years."""
    if beginning_value <= 0 or ending_value < 0 or years <= 0:
        raise ValueError("beginning_value and years must be positive, and ending_value non-negative")
    cagr = ((float(ending_value) / float(beginning_value)) ** (1.0 / float(years))) - 1.0
    return round(cagr * 100.0, 2)


def calculate_break_even_units(
    fixed_costs: Union[int, float],
    unit_price: Union[int, float],
    unit_variable_cost: Union[int, float],
) -> int:
    """Compute ceiling break-even unit volume given fixed costs, unit price, and unit variable cost."""
    if fixed_costs < 0 or unit_price <= 0 or unit_variable_cost < 0:
        raise ValueError("fixed_costs and unit_variable_cost must be non-negative and unit_price positive")
    contribution_margin = float(unit_price) - float(unit_variable_cost)
    if contribution_margin <= 0:
        raise ValueError("unit_price must exceed unit_variable_cost")
    raw_units = float(fixed_costs) / contribution_margin
    whole_units = int(raw_units)
    return whole_units if raw_units == whole_units else whole_units + 1





