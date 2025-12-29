What is Pandas used for in quant trading?
    Pandas is a Python library used for data handling and time-series analysis.
    In quant trading, Pandas is used to:
        Load market data (CSV, Excel, databases)
        Handle time-series data (dates, prices, volumes)
        Calculate indicators (moving averages, returns, volatility)
        Generate trading signals
        Backtest strategies
        Analyze performance (equity curves, drawdowns)

What is a DataFrame?
    A DataFrame is Pandas’ main data structure.
    Think of it as:
        An Excel spreadsheet
        A SQL table
        A time-indexed financial dataset


How .rolling() and .mean() work?
    These two functions are used together to compute moving averages.
        
        df['Close'].rolling(window=50).mean()

        Takes the last 50 closing prices
        Computes their average
        Assigns it to the current row
        Slides the window forward by 1 row