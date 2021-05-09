import csv
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("data2.csv")

print(df.groupby("female")["highschool_completed"].mean())
fig = go.Figure(go.Bar(x = df.groupby("female")["highschool_completed"].mean(), y=["1", "0"], orientation = "h"))
fig.show()