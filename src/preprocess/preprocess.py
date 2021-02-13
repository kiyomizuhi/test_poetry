import pandas as pd

import yaml
from pathlib import Path

import glob

if __name__ == "__main__":
    path_config = Path("src/config/config.yaml")

    with open(path_config, mode='r') as f:
        config = yaml.load(f, Loader=yaml.SafeLoader)

    df = pd.read_csv(
        './data/raw/breast-cancer-wisconsin.data',
        names=config["feature_names"]
        )

    df.to_csv("./data/interim/data.csv",
        encoding="utf-8",
        index=False
        )

