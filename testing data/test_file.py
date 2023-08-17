"""
CSE 163

Tests methods in CSE 163 project.
"""

import geopandas as gpd

from loadprojdata import RQ1_loading_data
from rq1 import sums_on_geos
from loadprojdata import RQ2_loading_data
from cse163_utils import assert_equals


def test_sums_on_geos(athlete_gdp_info: gpd.GeoDataFrame,
                      countries_shp: str) -> None:
    """
    Tests sum_on_geos method from RQ1.
    """
    assert_equals(3, sums_on_geos(athlete_gdp_info, countries_shp))
                        

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
    test_data = RQ1_loading_data(
        '/Users/tiaesperanzate/Desktop/cse 163/athlete_test_file.csv',
        '/Users/tiaesperanzate/Desktop/cse 163/athlete_test_file.csv')

    countries_shps = gpd.read_file('data/World_Countries_Generalized.shp')

    countries_shps = gpd.GeoDataFrame(countries_shps[
        countries_shps['country'].isin(['United States',
                                        'Australia',
                                        'Canada',
                                        'South Korea',
                                        'Russian Federation'])])

    test_sums_on_geos(test_data, countries_shps)
    test_RQ2_loading_data('data/athletes.csv',
                          'data/countries.csv',
                          'data/World_Countries_Generalized.shp',
                          'data/all.csv')


if __name__ == '__main__':
    main()
