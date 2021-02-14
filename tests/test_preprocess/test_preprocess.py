import pandas as pd
import pytest

from src.preprocess.preprocess import set_column_names


@pytest.mark.parametrize(
    "df,names",
    [(pd.DataFrame([[1, 2], [3, 4]]), ["a", "b"])],
)
def test_set_column_names(df, names):
    df = set_column_names(df, names)
    assert (df.columns == names).all(), "column names do not match!"
