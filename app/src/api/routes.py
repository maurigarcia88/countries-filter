from fastapi import APIRouter
from typing import Optional
import app.src.services.datasetexplorer as data_set_explorer

router = APIRouter()


@router.get("/countries-filter/greater-than/")
async def get_indicator_index_greater_than(
        indicator: str, value: float, inequality: Optional[str] = data_set_explorer.TOTAL_INEQUALITY_VALUE):
    """
    Return countries with corresponding index greater than indicated one.
    :param indicator: go to ./indicator-values to get valid values
    :param value: index value to compare with
    :param inequality: valid values: go to ./inequality-values to get valid values
    :return: dictionary with the result of previous matching conditions
    """
    return data_set_explorer.get_countries_by_index_greater_than(
        indicator=indicator,
        value=value,
        inequality=inequality
    )


@router.get("/countries-filter/indicator-values/")
async def get_indicator_valid_values():
    """Return INDICATOR column valid values"""
    return data_set_explorer.get_valid_indicators()


@router.get("/countries-filter/inequality-values/")
async def get_inequality_valid_values():
    """Return INEQUALITY column valid values"""
    return data_set_explorer.get_valid_inequalities()


@router.get("/")
async def read_main():
    """
    :return: dictionary with main instructions in msg key.
    """
    return {"msg": "Hello. This is an AIVO's challenge. Please open your browser at http://127.0.0.1:8000/docs"}
