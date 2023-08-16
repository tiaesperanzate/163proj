"""
CSE 163

Loads in and merges data
"""

import pandas as pd


def RQ1_loading_data(athlete_csv: str,
                     countries_csv: str) -> pd.DataFrame:
    """
    Reads in the athletes and countries csv data,
    returns the combined tables as one DataFrame
    """
    athlete_csv = pd.read_csv(athlete_csv)
    countries_csv = pd.read_csv(countries_csv)

    return athlete_csv.merge(countries_csv,
                             left_on='nationality',
                             right_on='code',
                             how='left')
