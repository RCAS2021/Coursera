import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html

# Reading airline data into pandas dataframe
airline_data = pd.read_csv(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv',
    encoding = 'ISO-8859-1',
    dtype={'Div1Airport': str, 'Div1TailNum': str,
            'Div2Airport': str, 'Div2TailNum':str})

# Randomly sample 500 data points, setting random state
data = airline_data.sample(n=500, random_state=42)

fig = px.pie(data, values='Flights', names='DistanceGroup', title='Distance group proportion by flights')

# Create a dash application
app = dash.Dash(__name__)

# Get the layout of the application and adjust it.
# Create an outer division using html.Div and add title to the dashboard using html.h1
# Add description about the graph using html P
# Finally, add the graph
app.layout = html.Div(children=[html.H1('Airline Dashboard', style={'texAlign': 'center',
                                                                    'color': '#504D36',
                                                                    'font-size': 40}),
                                html.P('Proportion of distance group (250 mile distance interval group) by flights.',
                                        style={'textAlign':'center', 'color':'#F57241'}),
                                dcc.Graph(figure=fig),])

# Run the app
if __name__ == '__main__':
    app.run_server()
