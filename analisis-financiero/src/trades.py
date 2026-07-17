import pandas as pd


def generate_trades(data, signal_column):

    trades = []

    position = 0
    entry_date = None
    entry_price = None


    for date, row in data.iterrows():

        signal = row[signal_column]
        price = row["Close"]


        # Entrada LONG
        if signal == 1 and position == 0:

            position = 1

            entry_date = date
            entry_price = price


        # Salida LONG
        elif signal != 1 and position == 1:

            position = 0

            exit_date = date
            exit_price = price


            trade_return = (
                exit_price /
                entry_price
                - 1
            ) * 100


            trades.append({

                "Entrada": entry_date,

                "Precio Entrada": entry_price,

                "Salida": exit_date,

                "Precio Salida": exit_price,

                "Retorno %": trade_return

            })


    return pd.DataFrame(trades)