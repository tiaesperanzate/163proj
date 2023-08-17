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


def rq3(data) -> None:
    """
    Reads in the athletes data to create a scatter plot
    Returns none
    """
    df = data.loc[:, ['gold', 'silver', 'bronze', 'height', 'weight']]
    df['total'] = df['gold'] + df['silver'] + df['bronze']
    print(df)
    fig = px.scatter(df, x='height', y='weight', color='total',
                     title="Olympic Athelete Measurements and Medals Won")
    fig.update_xaxes(title_text='Height (m)')
    fig.update_yaxes(title_text='Weight (kg)')
    fig.show()


def main():
    data = pd.read_csv('athletes.csv')
    rq3(data)


if __name__ == '__main__':
    main()
