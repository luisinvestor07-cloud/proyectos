import pandas as pd


def apply_strategy(data, signal_column, initial_capital=10000):

    df = data.copy()

    # Retorno diario del activo
    df["Return"] = df["Close"].pct_change()

    # Retorno de la estrategia
    df["Strategy Return"] = (
        df[signal_column].shift(1)
        *
        df["Return"]
    )

    # Curva de capital
    df["Portfolio"] = (
        initial_capital *
        (1 + df["Strategy Return"]).cumprod()
    )

    return df



def calculate_metrics(data):

    final_value = data["Portfolio"].iloc[-1]

    total_return = (
        final_value / data["Portfolio"].iloc[0]
        - 1
    )

    volatility = (
        data["Strategy Return"].std()
        *
        (252 ** 0.5)
    )


    sharpe = (
        data["Strategy Return"].mean()
        /
        data["Strategy Return"].std()
        *
        (252 ** 0.5)
    )


    return {
        "Valor Final": final_value,
        "Retorno Total": total_return,
        "Volatilidad": volatility,
        "Sharpe": sharpe
    }