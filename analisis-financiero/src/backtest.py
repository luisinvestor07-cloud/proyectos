import pandas as pd
import numpy as np


def apply_strategy(data, signal_column, initial_capital=10000):

    df = data.copy()

    # Retorno diario del activo
    df["Return"] = df["Close"].pct_change()

    # Retorno generado por la estrategia
    df["Strategy Return"] = (
        df[signal_column].shift(1)
        *
        df["Return"]
    )

    # El primer día no tiene retorno
    df["Strategy Return"] = (
        df["Strategy Return"]
        .fillna(0)
    )

    # Curva del capital
    df["Portfolio"] = (
        initial_capital *
        (1 + df["Strategy Return"]).cumprod()
    )

    return df



def calculate_metrics(data):

    final_value = (
        data["Portfolio"]
        .iloc[-1]
    )


    initial_value = (
        data["Portfolio"]
        .iloc[0]
    )


    total_return = (
        final_value /
        initial_value
        - 1
    )


    volatility = (
        data["Strategy Return"]
        .std()
        *
        np.sqrt(252)
    )


    sharpe = (
        data["Strategy Return"].mean()
        /
        data["Strategy Return"].std()
        *
        np.sqrt(252)
    )


    return {

        "Valor Final": final_value,

        "Retorno Total": total_return,

        "Volatilidad": volatility,

        "Sharpe": sharpe

    }



def calculate_drawdown(data):

    peak = (
        data["Portfolio"]
        .cummax()
    )

    drawdown = (
        data["Portfolio"] - peak
    ) / peak


    return drawdown.min()



def count_trades(data, signal_column):

    changes = (
        data[signal_column]
        .diff()
        .abs()
        .sum()
    )


    trades = changes / 2


    return int(trades)
def run_backtest(data, signal_column, strategy_name, initial_capital=10000):

    result = apply_strategy(
        data,
        signal_column,
        initial_capital
    )


    metrics = calculate_metrics(result)


    drawdown = calculate_drawdown(result)


    trades = count_trades(
        result,
        signal_column
    )


    report = {

        "Estrategia": strategy_name,

        "Capital Final": round(
            metrics["Valor Final"],
            2
        ),

        "Retorno %": round(
            metrics["Retorno Total"] * 100,
            2
        ),

        "Volatilidad %": round(
            metrics["Volatilidad"] * 100,
            2
        ),

        "Sharpe": round(
            metrics["Sharpe"],
            2
        ),

        "Drawdown %": round(
            drawdown * 100,
            2
        ),

        "Operaciones": trades

    }


    return result, report