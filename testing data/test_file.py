"""
CSE 163

Tests methods in CSE 163 project.
"""

import geopandas as gpd

from loadprojdata import RQ2_loading_data
from cse163_utils import assert_equals


def test_RQ2_loading_data(athletes_csv: str,
                          countries_csv: str,
                          world_shp: str,
                          iso_to_country_csv: str) -> None:
    """
    Tests RQ2_loading_data from loadprojdata.
    """
    assert_equals((111, 22), RQ2_loading_data(athletes_csv,
                                              countries_csv,
                                              world_shp,
                                              iso_to_country_csv).shape)


def main():
    test_RQ2_loading_data('data/athletes.csv',
                          'data/countries.csv',
                          'data/World_Countries_Generalized.shp',
                          'data/all.csv')


if __name__ == '__main__':
    main()
