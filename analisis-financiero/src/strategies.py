def sma_rsi_strategy(data):

    signal = (
        (data["SMA20"] > data["SMA50"]) &
        (data["RSI"] < 70)
    )

    data["Signal"] = 0
    data.loc[signal, "Signal"] = 1

    return data