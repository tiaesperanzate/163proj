











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
