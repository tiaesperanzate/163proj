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
import loadprojdata


def RQ2_map(project_data: gpd.GeoDataFrame) -> None:
    """
    Takes in GeoDataFrame of the project data
    and creates a map showing the female athletes
    sent to 2016 olympics by country and male athletes
    sent to 2016 olypmics by country side by side.
    """
    fig, [ax1, ax2] = plt.subplots(nrows=2)
    project_data.plot(color='#EEEEEE', ax=ax1)
    project_data.plot(column='sex_female', ax=ax1, legend=True)
    project_data.plot(color='#EEEEEE', ax=ax2)
    project_data.plot(column='sex_male', ax=ax2, legend=True)

    ax1.set_title('Female Athletes Sent to 2016 Olympics by Country')
    ax2.set_title('Male Athletes Sent to 2016 Olympics by Country')
    plt.subplots_adjust(hspace=0.5)

    plt.savefig('RQ2maps.png')


def main():
    RQ2_data = loadprojdata.RQ2_loading_data(
        'data/athletes.csv',
        'data/countries.csv',
        'data/World_Countries_Generalized.shp',
        'data/all.csv'
    )
    RQ2_map(RQ2_data)


if __name__ == '__main__':
    main()
