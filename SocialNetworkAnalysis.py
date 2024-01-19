import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns


file_path = 'data.csv'

data = pd.read_csv(file_path)

print(data.head())

data['Posts'] = pd.to_numeric(data['Posts'].str.replace('K', 'e3').str.replace('M', 'e6'), errors='coerce')


print(data['Posts'])
print(data['Posts'].describe())



G = nx.from_pandas_edgelist(data, source='name', target='Category')


print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")
print(f"Graph density: {nx.density(G)}")
"""
density = 2 * |E| / (|V| * (|V| - 1))
"""


plt.figure(figsize=(12, 8))
nx.draw(G, with_labels=True, font_size=15, node_size=120, font_color='red')
plt.title('Social Network Analysis')
plt.show()


category_counts = data['Category'].value_counts()
"""
Entertainment    4
Photography      3
Health           3
"""
 

print("\nCategory-wise Analysis:")
print(category_counts)


plt.figure(figsize=(12, 8))
sns.barplot(x=category_counts.index, y=category_counts.values, palette='viridis')#color palette in Seaborn.
plt.title('Category-wise Analysis')
plt.xticks(rotation=45)
plt.show()

degree_centrality = nx.degree_centrality(G)
"""
C(v)=(Total number of nodes)/(Number of incoming edges to v)
"""
degree_df = pd.DataFrame.from_dict(degree_centrality, orient='index', columns=['Degree Centrality'])

degree_df = degree_df.sort_values(by='Degree Centrality', ascending=False)
print(degree_df.head())

betweenness_centrality = nx.betweenness_centrality(G)
betweenness_df = pd.DataFrame.from_dict(betweenness_centrality, orient='index', columns=['Betweenness Centrality'])
betweenness_df = betweenness_df.sort_values(by='Betweenness Centrality', ascending=False)
print(betweenness_df.head())


closeness_centrality = nx.closeness_centrality(G)
closeness_df = pd.DataFrame.from_dict(closeness_centrality, orient='index', columns=['Closeness Centrality'])
closeness_df = closeness_df.sort_values(by='Closeness Centrality', ascending=False)
print(closeness_df.head())


plt.figure(figsize=(12, 8))
sns.barplot(x=degree_df.index, y=degree_df['Degree Centrality'], palette='viridis')
plt.title('Degree Centrality')
plt.xticks(rotation=90)
plt.show()


plt.figure(figsize=(12, 8))
sns.barplot(x=betweenness_df.index, y=betweenness_df['Betweenness Centrality'], palette='viridis')
plt.title('Betweenness Centrality')
plt.xticks(rotation=90)
plt.show()


plt.figure(figsize=(12, 8))
sns.barplot(x=closeness_df.index, y=closeness_df['Closeness Centrality'], palette='viridis')
plt.title('Closeness Centrality')
plt.xticks(rotation=90)
plt.show()

