import requests
import pandas as pd
from datetime import datetime, timedelta
import os

def download_station_data(station_id, start_date, end_date):
    """
    Download data for a specific station from NOAA's API
    """
    base_url = "https://www.ncei.noaa.gov/access/services/data/v1"
    
    params = {
        'dataset': 'daily-summaries',
        'stations': station_id,
        'startDate': start_date,
        'endDate': end_date,
        'format': 'csv',
        'units': 'metric',
        'includeAttributes': 'false'
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        with open(f'data/{station_id}.csv', 'w') as f:
            f.write(response.text)
        print(f"Successfully downloaded data for station {station_id}")
    else:
        print(f"Failed to download data for station {station_id}")

def main():
    # Create data directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')
    
    # Station IDs
    stations = [
        "USW00014837",  # MADISON DANE CO REGIONAL AIRPORT, WI US
        "USW00014898",  # MILWAUKEE MITCHELL INTL AIRPORT, WI US
        "USW00014920",  # GREEN BAY AUSTIN STRAUBEL INTERNATIONAL AIRPORT, WI US
        "USW00014991"   # EAU CLAIRE REGIONAL AIRPORT, WI US
    ]
    
    # Date range (last 30 years)
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=365*30)).strftime('%Y-%m-%d')
    
    # Download data for each station
    for station in stations:
        download_station_data(station, start_date, end_date)

if __name__ == "__main__":
    main() 