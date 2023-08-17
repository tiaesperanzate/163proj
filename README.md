# Final Project: Analyzing Olympic Performance and Determinants 


Contributors: Shira Zur, Tia Esperanzate, Danika Lee

CSE 163: Intermediate Programming

Document Including Full Report Details: [Link](https://docs.google.com/document/d/1-WX610mWzgdk_J6iKu3qSaJfSawU6yLwcKdOqzOj058/edit)

## About the Files

* **rq1.py** - Answers research Question 1 "Is there a relationship between GDP per capita and the amount of awarded medals of
certain countries in 2016?"

    * Calculates medals awarded by country and normalizes
the counts for comparison

    * Creates a scatterplot showing
relationship between GDP and medals won
    * Creates
choropleth maps showing GDP data across different
countries and medal distribution.

* **rq2.py** - Answer research Question 2 "Is there a relationship between the country sending the athlete and the athlete's sex?"

    * Creates maps for female athletes per country and male athletes per country

* **loadprojdata.py**
    * Loads in and merges the athletes and countries datasets

## Libraries Necessary for Installation

* Pandas
* GeoPandas
* MatPlotLib
* Plotly
> Installation Line: pip install plotly

> Installation Line: pip install -U kaleido



## Required Data

Data Sources: [Kaggle](https://olympics.com/en/olympic-games/rio-2016) and [ArcGIS Hub](https://hub.arcgis.com/datasets/esri::world-countries-generalized/explore?location=-1.481530%2C-167.596765%2C1.98)

* **athletes.csv** - contains information about athletes who competed in the Rio de Janeiro, 2016 Olympics collaborated by Rio 2016 (link to [Download](https://www.kaggle.com/datasets/rio2016/olympic-games?select=athletes.csv))
* **countries.csv** - contains country, country population, and country GDP information for 2016 (link to [Download](https://www.kaggle.com/datasets/rio2016/olympic-games?select=countries.csv))
* **World_Countries_Generalized.shp** - contains details and geometries for mapping/plotting shapes of all countries (link to [Download](https://hub.arcgis.com/datasets/esri::world-countries-generalized/explore?location=-0.306120%2C12.403235%2C1.98))
* **all.csv** - contains countries and their code and iso code (link to [Download](https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes/blob/master/all/all.csv))


## How to Reproduce Our Results
1. Download the files listed above and save the data into the same folder containing our project files.

2. Run the following codes in the command/installation line

```Python
%pip install plotly
```
```Python
$ pip install -U kaleidoscope
```

3. Run the file *loadprojdata.py* to get the function for merging the athlete and countries csv datasets

4. Run the file *rq1.py* for research question 1 analysis

5. Run the file *rq2.py* for resarch question 2 analysis
   
