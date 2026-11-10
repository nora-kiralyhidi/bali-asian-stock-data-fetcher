# Bali – Asian Stock Market Data Fetcher

Bali is a small Python project that collects and stores recent price data for 46 Chinese companies listed in Hong Kong, Shanghai, Shenzhen and the United States. It is the first building block (the "Data Fetcher") of a larger, planned multi-agent analysis system.

This is a learning project. I am building it step by step, with the help of AI assistants, and I make sure I understand and can explain every part of the code.

## What it does

- Downloads the last 5 trading days of prices for each ticker with `yfinance`
- Calculates the latest closing price and the 5-day percentage change
- Saves the results to a local SQLite database (one row per ticker per day; running the script again on the same day updates the rows instead of duplicating them)
- Prints a report sorted by sector
- Handles missing data and errors, and lists the tickers that failed

## Coverage

| Market | Tickers |
|---|---|
| Hong Kong (`.HK`) | 16 |
| Shanghai (`.SS`) | 9 |
| Shenzhen (`.SZ`) | 9 |
| Chinese companies listed in the US | 12 |

Sectors include tech/AI, automotive, finance, semiconductors, energy, renewable energy, e-commerce and more.

## Tech stack

Python · pandas · yfinance · SQLite

## Project structure

| File | Purpose |
|---|---|
| `asia_app.py` | Main script: downloads data, builds the report |
| `bali_memory.py` | SQLite layer: creates the database and saves reports |
| `check_db.py` | Small helper that counts the rows in the database |

## How to run

```bash
pip install pandas yfinance
python asia_app.py
```

The database file `bali_data.db` is created automatically on the first run. To check how many rows it contains:

```bash
python check_db.py
```

## Known limitations

- `yfinance` is an unofficial data source (it reads Yahoo Finance data). Data can be incomplete, delayed or change without notice, so this project is meant for learning and personal experimentation.
- Data validation is still basic.
- Bali is currently a data collection and processing script. It is not yet an AI agent.
- The output is data and analysis only, **not investment advice**.

## Roadmap

- [ ] Stronger data validation
- [ ] Charts and generated reports
- [ ] Automatic daily run
- [ ] Analysis of the collected data
- [ ] Cloud deployment on AWS (scheduled run, storage)
- [ ] AI-agent functions and a multi-agent team (researcher, analyst, tester, coder, coordinator)

## Author

Built by Királyhidi Nóra as part of a career change toward AI and cloud development.
