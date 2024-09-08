# Trading Strategy Project

This project implements a **Simple Moving Average (SMA) Crossover Strategy** using Python and provides buy/sell signals based on the crossover of two SMAs. The project includes data validation through unit testing, ensuring the correct data types for the input dataset.

## Project Overview

In this project, we calculate two SMAs—one short-term (20 days) and one long-term (50 days)—for stock price data. When the short-term SMA crosses above the long-term SMA, a **buy signal** is generated, and when the short-term SMA crosses below, a **sell signal** is generated.

### Features:
- Load stock data from CSV.
- Calculate 20-day and 50-day SMAs.
- Generate buy and sell signals.
- Plot price and SMA values.
- Unit tests for data type validation.

## Prerequisites

- Python 3.x
- Pandas
- Matplotlib
- MySQL Connector

You can install the required packages using pip:

```bash
pip install pandas matplotlib mysql-connector-python
```
## File Structure
```
trading_strategy_project/
├── data/
│   └── data.csv
├── scripts/
│   ├── insert_data.py
│   ├── sma_strategy.py
│   └── unit_tests.py
├── sql/
│   ├── create_tabel.sql
└── README.md
```
## Getting Started
1. **Prepare the CSV File:**
   Ensure your CSV file (data/data.csv) contains the following columns: datetime, close, high, low, open, volume, and instrument.

2. **Run the Data Insertion Script:**
   This script loads data from the CSV file into a MySQL database.
   ````
   python scripts/insert_data.py
3. **Run the SMA Strategy Script:**
   This script calculates SMAs, generates buy/sell signals, and plots the results.
   ````
   python scripts/sma_strategy.py
   ````
4. **Run Unit Tests:**
   This script validates data types in the CSV file.
   ````
   python scripts/unit_tests.py

