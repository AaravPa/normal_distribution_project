import pandas as pd
import csv
import plotly.figure_factory as ff

df=pd.read_csv("/Users/Kartik/Downloads/mobile_brand_data.csv")

fig=ff.create_distplot([df["Avg Rating"]], ["average rating"])
fig.show()
