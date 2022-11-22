"""
1. Geospatial data- geographic component(coordinates), lat, long, elevation
- Reading and exploring - geopandas library
EDA - Clusters and patterns, compare attrs across different regions
- Projections

- Visualization - Scatter plots, Choropleth maps

pip install Basemap
m = Basemap(projection="merc", llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
m.drawcoastlines()
m.fillcontinents(color="coral", lake_color="aqua")
m.drawparallels(np.arange(-90, 91, 30))
m.drawmeridians(np.arange(-180, 181, 60))
m.drawmapboundary(fill_color="aqua")
plt.show()

Choropleth maps - geopandas library

Analyzing maps and algorithms:
KDE - Kernel density estimation
kMeans Clustering
Hierarchical Clustering
kNN - k Nearest neighbors

2. Network analysis
- Graphs - Nodes (Vertex, points) which describe objects, Edges - connect the nodes
- Types of graphs - directed/undirected, weighted/unweighted

- Shortest path between nodes
- Centrality
- Communities
"""