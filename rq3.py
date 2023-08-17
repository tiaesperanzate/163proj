"""
Danika Lee
CSE 163

Group project: Research Question 3 filters relvant data from
athlete.csv dataset. Calculates the total medals won from each athlete.
Creates a plotly scatter plot that takes athlete height and weight,
each dot color corresponding to number of medals was won
(ex. blue for zero, yellow for six, etc.). The plot will show if there
is a relationship between athlete measurements and medals won.
"""
import pandas as pd
import plotly.express as px


def rq3(data: pd.DataFrame) -> None:
    """
    Reads in the athletes data to create a scatter plot
    Returns none
    """
    df = data.loc[:, ['gold', 'silver', 'bronze', 'height', 'weight']]
    df['total'] = df['gold'] + df['silver'] + df['bronze']
    df = df[df['total'] >= 1]
    fig = px.scatter(df, x='height', y='weight', color='total',
                     title="Olympic Athlete Measurements and Medals Won")
    fig.update_xaxes(title_text='Height (m)')
    fig.update_yaxes(title_text='Weight (kg)')
    fig.show()


def main():
    data: pd.read_csv('athletes.csv')
    rq3(data)


if __name__ == '__main__':
    main()
