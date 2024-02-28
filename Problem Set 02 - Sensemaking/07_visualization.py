# -----------------------------------------------
#  7. Data Visualization:
#  Objective: Visualize the word frequencies
#  using a visualization library.
# 
#  Tools/Resources: Examples of visualization 
#  libraries D3, Plotly, and Chart.JS.
#     D3, https://d3js.org/
#     Plotly, https://plotly.com/
#     Chart.JS, https://www.chartjs.org/
#     Google Charts, https://developers.google.com/chart/
# -----------------------------------------------

import pandas as pd
import plotly.graph_objects as go

# Load the data from the CSV file into a pandas DataFrame
df = pd.read_csv('department_word_frequencies.csv')
df = df.dropna()  # Remove rows with NaN values

# Filter the DataFrame to only include rows where the "Frequency" is 10 or greater
df = df[df['Frequency'] >= 10]

# Create unique IDs
df['ID'] = df['Department Index'] + '-' + df['Word']


# Create a DataFrame for the parent nodes
df_parent = pd.DataFrame({
    'labels': df['Department Index'].unique(),
    'parents': ['']*df['Department Index'].nunique(),
    'values': [0]*df['Department Index'].nunique(),
    'ids': df['Department Index'].unique()
})

# Create a DataFrame for the child nodes
df_child = pd.DataFrame({
    'labels': df['Word'],
    'parents': df['Department Index'],
    'values': df['Frequency'],
    'ids': df['ID']
})

df_sunburst = pd.concat([df_parent, df_child])
# print (df_sunburst)

# Create a sunburst chart
fig = go.Figure(go.Sunburst(
    ids=df_sunburst['ids'],
    labels=df_sunburst['labels'],
    parents=df_sunburst['parents'],
    values=df_sunburst['values'],
))

fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))

fig.show()