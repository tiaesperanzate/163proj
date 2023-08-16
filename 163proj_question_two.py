"""
Shira Zur
CSE 163

Research Question 2 for group project,
creates a map of the female athletes sent to
2016 Olympics by country and of the male
athletes sent to 2016 Olympics by country.
"""

import geopandas as gpd
import matplotlib.pyplot as plt
import plotly.express as px

import loadprojdata











def main():
    RQ2_data = loadprojdata.RQ2_loading_data(
        'data/athletes.csv',
        'data/countries.csv'
    )
    rq2_map(sums_on_geos(RQ1_data,
                             '/Users/tiaesperanzate/Desktop/cse 163/'
                             'World_Countries_Generalized/'
                             'World_Countries_Generalized.shp'))



if __name__ == '__main__':
    main()
