# Python for AI & Data Analytics Foundations

A collection of Python data analysis pipelines, weather & sales telemetry scripts, and algorithmic problem-solving modules built for AI and Data Science foundations.

## Modules Overview

| Path | Description |
| :--- | :--- |
| `data/sales-analysis/analyzer.py` | Pandas-based product sales revenue aggregation and currency reporting pipeline. |
| `data/sales-analysis/helpers.py` | Reusable revenue calculation (`calculate_total`) and currency formatting (`format_currency`) utilities. |
| `data/paris_weather.csv` & `data/gaziveren_weather.csv` | Comparative historical meteorological datasets used for time-series visualization (`weather_chart.png`). |
| `leetcode.py` | Core array, matrix wealth aggregation, and student grade analytics algorithms. |
| `gre.py` / `practice2.py` | Interactive Python data structures and control-flow exercises. |
| `tests/` | Automated `pytest` verification suite covering sales helpers and algorithmic modules. |

## Quick Start

```bash
pip install -r requirements.txt
pytest tests/ -v
```
