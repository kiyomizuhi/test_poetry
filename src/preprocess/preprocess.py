from pathlib import Path
from typing import List

import pandas as pd
import yaml


def set_column_names(df: pd.DataFrame, names: List[str]) -> pd.DataFrame:
    """
    Arguments:
    ----------
        df : input dataframe
        names : list of column names

    Returns:
    -------
        df : dataframe with column names with names
    """

    df.columns = names
    return df


if __name__ == "__main__":
    path_config = Path("src/config/config.yaml")

    with open(path_config, mode="r") as f:
        config = yaml.load(f, Loader=yaml.SafeLoader)

    df = pd.read_csv(
        "./data/raw/breast-cancer-wisconsin.data", names=config["feature_names"]
    )

    df.to_csv("./data/interim/data.csv", encoding="utf-8", index=False)
