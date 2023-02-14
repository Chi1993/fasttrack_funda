import dash
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("data/amsterdam.csv")


app = dash.Dash(__name__)

# Define the app
app.layout = html.Div()

property_type = list(df["property_type"].unique())


def price_area():
    # Function for creating line chart showing Google stock prices over time
    fig = go.Figure(
        [
            go.Scatter(
                x=df["area"],
                y=df["price"],
                line=dict(color="firebrick", width=4),
                name="Area Price",
                mode="markers",
            )
        ]
    )
    fig.update_layout(
        title="Prices over area", xaxis_title="area", yaxis_title="x 1000 Euro"
    )
    return fig


@app.callback(
    dash.Output("price-area-graph", "figure"),
    dash.Input("property-selection", "value"),
)
def update_price_area_graph(selected_property_type):
    if not selected_property_type:
        return {}

    data = df[df["property_type"].isin(selected_property_type)]

    fig = px.scatter(
        data,
        x="area",
        y="price",
        color="property_type",
    )

    fig.update_layout(
        title="Prices over area", xaxis_title="area", yaxis_title="x 1000 Euro"
    )
    return fig


app.layout = html.Div(
    id="parent",
    children=[
        html.H1(
            id="H1",
            style={"textAlign": "center", "marginTop": 40, "marginBottom": 40},
        ),
        dash.dcc.Dropdown(id="property-selection", options=property_type, multi=True),
        dash.dcc.Graph(id="price-area-graph"),
    ],
)

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
