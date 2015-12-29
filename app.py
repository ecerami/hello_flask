from flask import Flask, render_template

import json
import plotly

import pandas as pd
import numpy as np
import plotly.graph_objs as go

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    # Read in the Data via Pandas
    df = pd.read_table("data/fruit.txt")
    
    # Create the Plotly Data Structure
    graph = dict(
        data=[go.Bar(
            x=df["fruit"],
            y=df["count"]
        )],
        layout=dict(
            title='Bar Plot',
            yaxis=dict(
                title="Count"
            ),
            xaxis=dict(
                title="Fruit"
            )
        )
    )

    # Convert the figures to JSON
    graphJSON = json.dumps(graph, cls=plotly.utils.PlotlyJSONEncoder)

    # Render the Template
    return render_template('layouts/index.html', graphJSON=graphJSON)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)
