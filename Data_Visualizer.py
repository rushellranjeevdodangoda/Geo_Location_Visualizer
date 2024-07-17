# This code reads the CSV file that contains details about the Airports in Thailand and then visualizes them on Google Earth 

# Importing the necessary libraries
import pandas as pd 
import simplekml
import subprocess
import os

# Try loading the dataset with different encodings
encodings = ['utf-8', 'latin1', 'iso-8859-1', 'cp1252'] 
for encoding in encodings:
    try:
        df_Locations = pd.read_csv('th-airports.csv', encoding=encoding)
        print(f"Successfully loaded CSV with {encoding} encoding")
        break
    except UnicodeDecodeError as e:
        print(f"Failed to load CSV with {encoding} encoding: {e}")

# URL of the custom icon
icon_url = "plane.png" 

# Create a KML object
kml = simplekml.Kml()

# Loop through the dataframe and create KML points for each airport
for index, row in df_Locations.iterrows():
    pnt = kml.newpoint(name=row['name'], coords=[(row['longitude_deg'], row['latitude_deg'])])
    pnt.style.iconstyle.icon.href = icon_url

# Save the KML file
kml_file = os.path.abspath('thailand_airports.kml')
kml.save(kml_file)

print(f"KML file created successfully at {kml_file}")

# Automatically open the KML file with Google Earth
try:
    if os.name == 'nt':  # For Windows
        subprocess.Popen(['C:\\Program Files\\Google\\Google Earth Pro\\client\\googleearth.exe', kml_file])
    elif os.name == 'posix':  # For macOS or Linux
        subprocess.Popen(['open', '-a', 'Google Earth', kml_file])
    print("Google Earth is opening the KML file.")
except Exception as e:
    print(f"Failed to open KML file with Google Earth: {e}")
