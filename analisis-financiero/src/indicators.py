import pandas as pd


def calculate_sma(data, period=20):
    return data["Close"].rolling(period).mean()


def calculate_returns(data):
    return data["Close"].pct_change()


def calculate_volume_average(data, period=20):
    return data["Volume"].rolling(period).mean()