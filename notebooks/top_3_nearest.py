# Return 3 nearest station/school/park ... to your property
import pandas as pd
from geopy.distance import geodesic

class LocationFinder:
    def __init__(self):
        pass
    
    def top_3_nearest(self, latitude, longitude, csv_file_path):
        """
        Teke in three variables: latitude(of rental property), longitude(of rental property), csv_file_path(path to train station/school/parks files)
        Calculate the top 3 nearest location and return in dataframe
        """
        # Load the location data from the CSV file into a dataframe
        location_df = pd.read_csv(csv_file_path)
        
        # Define a function to calculate the distance between two lat/long pairs
        def calculate_distance(row):
            return geodesic((latitude, longitude), (row['latitude'], row['longitude'])).kilometers
        
        # Apply the distance calculation to the dataframe
        location_df['distance'] = location_df.apply(calculate_distance, axis=1)
        
        # Sort by distance and return the top 3 nearest locations
        top_3_nearest_locations = location_df.sort_values(by='distance').head(3)
        
        return top_3_nearest_locations


