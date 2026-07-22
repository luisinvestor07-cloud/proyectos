from indicators import add_indicators


def sma_rsi_strategy(data):

    required = ("SMA20", "SMA50", "RSI")
    if not all(col in data.columns for col in required):
        data = add_indicators(data)

    signal = (
        (data["SMA20"] > data["SMA50"]) &
        (data["RSI"] < 70)
    )

    data["Signal"] = 0
    data.loc[signal, "Signal"] = 1

    return data