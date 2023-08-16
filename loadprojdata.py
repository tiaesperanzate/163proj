"""
CSE 163

Loads in and merges data
"""

import pandas as pd
import geopandas as gpd


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
                       
def RQ2_loading_data(athletes_csv: str, countries_csv: str,
                     world_shp: str, iso_to_country_csv: str) -> gpd.DataFrame:
    athletes_df = pd.read_csv(athletes_csv)
    countries_df = pd.read_csv(countries_csv)
    athletes_countries_merged = pd.merge(athletes_df, countries_df, 
                                         left_on='nationality', 
                                         right_on='code')
    sex_data = pd.get_dummies(athletes_countries_merged[['nationality', 'sex']],
                              columns=['sex']).groupby('nationality').sum().reset_index()
    world_data = gpd.read_file(world_shp)
    iso_to_country = pd.read_csv(iso_to_country_csv)
    geo_data = world_data.merge(
            iso_to_country,
            left_on="ISO",
            right_on="alpha-2",
            how="left"
        )
    project_data = sex_data.merge(
        geo_data, left_on="nationality",
        right_on="alpha-3",
        how="inner"
    )
    project_data = gpd.GeoDataFrame(project_data, geometry='geometry')
    return project_data
