import pandas as pd


def calculate_sma(data, period=20):
    return data["Close"].rolling(period).mean()


def calculate_returns(data):
    return data["Close"].pct_change()


def calculate_volume_average(data, period=20):
    return data["Volume"].rolling(period).mean()


def calculate_rsi(data, period=14):
    delta = data["Close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return rsi


def add_indicators(data):
    df = data.copy()

    df["SMA20"] = calculate_sma(df, 20)
    df["SMA50"] = calculate_sma(df, 50)
    df["RSI"] = calculate_rsi(df, 14)

    return df