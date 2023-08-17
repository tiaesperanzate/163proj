"""
CSE 163

Tests sums_on_geos in rq1.py
"""

import geopandas as gpd

from loadprojdata import RQ1_loading_data
from rq1 import sums_on_geos
from cse163_utils import assert_equals


def test_sums_on_geos(athlete_gdp_info: gpd.GeoDataFrame,
                      countries_shp: str) -> None:
    assert_equals(3, sums_on_geos(athlete_gdp_info, countries_shp))


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


if __name__ == '__main__':
    main()
