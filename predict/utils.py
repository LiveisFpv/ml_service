import pandas as pd


def columnsToDateFormat(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    for col_name in cols:
        df[col_name] = pd.to_datetime(df[col_name])
    return df
