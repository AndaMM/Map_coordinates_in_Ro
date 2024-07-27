import pandas as pd
import geopandas as gpd
import folium
import os

#Read the data from the CSV file
file_path = r"romania_coordinates.csv"
print(f"Reading CSV file from: {file_path}")
df = pd.read_csv(file_path)

#Create a GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude))

#Create a folium map centered around Romania
romania_center = [46.3100, 25.0700]  # Latitude and Longitude for Romania's center
map = folium.Map(location=romania_center, zoom_start=7, tiles='CartoDB Positron')  # Adjust zoom_start as needed

#Add markers to the map
for idx, row in gdf.iterrows():
    folium.Marker([row.geometry.y, row.geometry.x],
                  popup=folium.Popup(f"<b>Annotation:</b> {idx}<br><b>Latitude:</b> {row.geometry.y}<br><b>Longitude:</b> {row.geometry.x}", max_width=250),
                  tooltip=f"Index: {idx}",
                  icon=folium.Icon(color='blue')).add_to(map)

# Save the map in the directory
output_path = r'romania_map.html'
print(f"Saving map to: {output_path}")
map.save(output_path)

# Verify the current working directory (for debugging purposes)
print("Current Working Directory:", os.getcwd())
print(f"Map should be saved at: {output_path}")
