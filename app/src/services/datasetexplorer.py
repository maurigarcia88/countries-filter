import pandas as pd
from app.src.api.exceptions import DataSetKeyValueError
DATA_SET_PATH = "./app/src/data/BLI_28032019144925238.csv"

data_set = pd.read_csv(DATA_SET_PATH)
unique_indicators = data_set.INDICATOR.unique()
unique_inequalities = data_set.INEQUALITY.unique()

TOTAL_INEQUALITY_VALUE = "TOT"


def get_countries_by_index_greater_than(indicator: str, inequality: str, value: float, ) -> dict:
    """
    Return countries which indicator index is greater than value
    """
    if _validate_indicator(indicator) and _validate_inequality(inequality):
        filter_series = (data_set.INDICATOR == indicator) & \
                        (data_set.INEQUALITY == inequality) & \
                        (data_set.Value > value)
        return dict(zip(data_set.Country[filter_series], data_set.Value[filter_series]))
    else:
        return DataSetKeyValueError


def get_valid_indicators() -> list:
    """Return unique INDICATOR column values as list"""
    return unique_indicators.tolist()


def get_valid_inequalities():
    """Return unique INEQUALITY column values as list"""
    return unique_inequalities.tolist()


def _validate_indicator(indicator: str):
    """Return if indicator is in INDICATOR column or not"""
    return indicator in unique_indicators


def _validate_inequality(inequality: str):
    """Return if inequality is in INEQUALITY column or not"""
    return inequality in unique_inequalities
