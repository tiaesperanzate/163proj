"""
Tia Esperanzate
CSE 163

Research Question 1 for group project,
calculates medals awarded by country and normalizes
the counts for comparison, creates a scatterplot showing
relationship between GDP and medals won, and creates
choropleth maps showing GDP data across different
countries and medal distribution.
"""

import geopandas as gpd
import matplotlib.pyplot as plt
import plotly.express as px

import loadprojdata


def sums_on_geos(athlete_gdp_info: gpd.GeoDataFrame,
                 countries_shp: str) -> gpd.GeoDataFrame:
    """
    Takes a GeoDataFrame and countries shape file to
    add the total medals by country and divide by population
    to normalize the medal counts by population, joins the
    new calculations to the given GeoDataFrame and returns
    the new GeoDataFrame.
    """
    athlete_gdp_info['medal_count'] = (athlete_gdp_info['gold'] +
                                       athlete_gdp_info['silver'] +
                                       athlete_gdp_info['bronze'])
    medals_per_country = athlete_gdp_info.groupby('code')['medal_count'].sum()

    pop_gdp_table = athlete_gdp_info.loc[:, ['country',
                                             'code',
                                             'population',
                                             'gdp_per_capita']]
    pop_gdp_table.loc[pop_gdp_table['country'] == 'Korea, South',
                      'country'] = 'South Korea'
    pop_gdp_table.loc[pop_gdp_table['country'] == 'Russia',
                      'country'] = 'Russian Federation'
    country_data = pop_gdp_table.merge(medals_per_country,
                                       on='code',
                                       how='left')
    country_data['normalized_medal_values'] = (country_data['medal_count'] /
                                               country_data['population'])
    no_nas = country_data.dropna().drop_duplicates()
    no_nas['country'] = no_nas['country'].str.rstrip('*')

    countries_shp = gpd.read_file(countries_shp)
    country_medal_data = no_nas.merge(countries_shp,
                                      left_on='country',
                                      right_on='COUNTRY',
                                      how='right')
    return gpd.GeoDataFrame(country_medal_data, geometry='geometry')


def rq1_scatter(medal_geodata: gpd.GeoDataFrame) -> None:
    """
    Takes a GeoDataFrame and creates an interactive
    scatterplot with country gdp on the y-axis and
    normalized medal values on the x-axis. Returns None.
    """
    plot1 = px.scatter(medal_geodata,
                       y="gdp_per_capita",
                       x="normalized_medal_values",
                       hover_data=['country'],
                       trendline="ols")
    plot1.update_xaxes(title_text='Medals Won by Country Population')
    plot1.update_yaxes(title_text='Gross Domestic Product (GDP)')
    plot1.update_layout(
        title='Relationships Between GDP and Medals awarded in 2016 Olympics',
        title_x=0.5
        )


def rq1_maps(medal_geodata: gpd.GeoDataFrame) -> None:
    """
    Takes a GeoDataFrame and creates 2 maps on
    one axis of GDP per country and medal distributions.
    Returns None.
    """
    fig, [ax1, ax2] = plt.subplots(nrows=2)
    medal_geodata.plot(color='#EEEEEE', ax=ax1)
    medal_geodata.plot(column='gdp_per_capita', ax=ax1, legend=True)
    medal_geodata.plot(color='#EEEEEE', ax=ax2)
    medal_geodata.plot(column='medal_count', ax=ax2, legend=True)

    ax1.set_title('GDP Per Capita by Country 2016')
    ax2.set_title('Country Total Medals Won in 2016 by Olympic Athletes')
    plt.subplots_adjust(hspace=0.5)

    plt.savefig('RQ1maps.png')


def main():
    RQ1_data = loadprojdata.RQ1_loading_data(
        '/Users/tiaesperanzate/Desktop/cse 163/athletes.csv',
        '/Users/tiaesperanzate/Desktop/cse 163/countries.csv'
    )
    rq1_scatter(sums_on_geos(RQ1_data,
                             '/Users/tiaesperanzate/Desktop/cse 163/'
                             'World_Countries_Generalized/'
                             'World_Countries_Generalized.shp'))
    rq1_maps(sums_on_geos(RQ1_data,
                          '/Users/tiaesperanzate/Desktop/cse 163/'
                          'World_Countries_Generalized/'
                          'World_Countries_Generalized.shp'))


if __name__ == '__main__':
    main()
