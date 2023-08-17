"""
Danika Lee
CSE 163

Group project: Research Question 3 filters relvant data from
athlete.csv dataset. Creates a plotly scatter plot that takes
athlete height and weight, each dot corresponding to which medal was won
(ex. Yellow for gold, grey for silver, orange for bronze). The plot will
show if there is a relationship between athlete measurements and medals
won.
"""
import pandas as pd
import plotly.express as px


def RQ3(data: DataFrame) -> None:
    """
    Reads in the atheletes data to create a scatter plot 
    Returns none
    """
    data = pd.read_csv('athletes.csv')
    col = ['gold', 'silver', 'bronze', 'height', 'weight']
    d = col[(col['gold'] >= 1) | (col['silver'] >= 1)
                     | (col['bronze'] >= 1)]
    medal_data = []
    for index, row in d.iterrows():
        if row['gold'] > 0:
            medal_data.append({'Medal': 'Gold', 'Height': row['height'], 'Weight': row['weight']})
        if row['silver'] > 0:
            medal_data.append({'Medal': 'Silver', 'Height': row['height'], 'Weight': row['weight']})
        if row['bronze'] > 0:
            medal_data.append({'Medal': 'Bronze', 'Height': row['height'], 'Weight': row['weight']})
    df = pd.DataFrame(medal_data)
    fig = px.scatter(df, x = 'Height', y = 'Weight', color = 'Medal'
                     title = "Olympic Athelete Measurements and Medals Won",
                     color_discrete_map={'Gold': 'gold', 'Silver': 'silver',
                     'Bronze': 'orange'})
    fig.update_xaxes(title_text='Height (m)')
    fig.update_yaxes(title_text='Weight (kg)')
    fig.show()
