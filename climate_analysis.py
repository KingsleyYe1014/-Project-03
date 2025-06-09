import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

# Set style for all plots
plt.style.use('default')
sns.set_theme(style="whitegrid")

# Create images directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Function to read and process data
def load_data(file_path):
    df = pd.read_csv(file_path)
    df['DATE'] = pd.to_datetime(df['DATE'])
    df['YEAR'] = df['DATE'].dt.year
    df['MONTH'] = df['DATE'].dt.month
    df['SEASON'] = pd.cut(df['MONTH'], 
                         bins=[0, 3, 6, 9, 12], 
                         labels=['Winter', 'Spring', 'Summer', 'Fall'])
    return df

# 1. Annual Temperature Analysis
def analyze_temperature(df):
    # Calculate annual mean temperature
    annual_temp = df.groupby('YEAR')['TAVG'].mean().reset_index()
    
    # Create the plot
    plt.figure(figsize=(12, 6))
    sns.regplot(data=annual_temp, x='YEAR', y='TAVG', scatter_kws={'alpha':0.5})
    plt.title('Annual Mean Temperature Trend')
    plt.xlabel('Year')
    plt.ylabel('Temperature (°C)')
    plt.grid(True, alpha=0.3)
    plt.savefig('images/annual_temperature_trend.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    return annual_temp

# 2. Precipitation Analysis
def analyze_precipitation(df):
    # Calculate annual precipitation
    annual_precip = df.groupby('YEAR')['PRCP'].sum().reset_index()
    
    plt.figure(figsize=(12, 6))
    sns.regplot(data=annual_precip, x='YEAR', y='PRCP', scatter_kws={'alpha':0.5})
    plt.title('Annual Precipitation Trend')
    plt.xlabel('Year')
    plt.ylabel('Total Precipitation (mm)')
    plt.grid(True, alpha=0.3)
    plt.savefig('images/annual_precipitation_trend.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    return annual_precip

# 3. Season Length Analysis
def analyze_seasons(df):
    # Calculate average temperature by year and season
    seasonal_temp = df.groupby(['YEAR', 'SEASON'])['TAVG'].mean().reset_index()
    
    plt.figure(figsize=(12, 6))
    for season in ['Spring', 'Summer', 'Fall', 'Winter']:
        season_data = seasonal_temp[seasonal_temp['SEASON'] == season]
        plt.plot(season_data['YEAR'], season_data['TAVG'], label=season, marker='o', alpha=0.6)
    
    plt.title('Seasonal Temperature Trends')
    plt.xlabel('Year')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('images/seasonal_temperature_trends.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    return seasonal_temp

# 4. Heat Wave Analysis
def analyze_heat_waves(df, threshold_temp=30):
    # Calculate number of heat wave days per year
    heat_wave_days = df[df['TMAX'] >= threshold_temp].groupby('YEAR').size().reset_index()
    heat_wave_days.columns = ['YEAR', 'HEAT_WAVE_DAYS']
    
    plt.figure(figsize=(12, 6))
    sns.regplot(data=heat_wave_days, x='YEAR', y='HEAT_WAVE_DAYS', scatter_kws={'alpha':0.5})
    plt.title(f'Annual Number of Heat Wave Days (T ≥ {threshold_temp}°C)')
    plt.xlabel('Year')
    plt.ylabel('Number of Days')
    plt.grid(True, alpha=0.3)
    plt.savefig('images/heat_wave_trend.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    return heat_wave_days

# Main analysis function
def main():
    # Load data for multiple stations
    stations = [
        "USW00014837",  # MADISON DANE CO REGIONAL AIRPORT, WI US
        "USW00014898",  # MILWAUKEE MITCHELL INTL AIRPORT, WI US
        "USW00014920",  # GREEN BAY AUSTIN STRAUBEL INTERNATIONAL AIRPORT, WI US
        "USW00014991"   # EAU CLAIRE REGIONAL AIRPORT, WI US
    ]
    
    # Perform analysis for each station
    for station in stations:
        try:
            df = load_data(f'data/{station}.csv')
            
            # Run analyses
            temp_results = analyze_temperature(df)
            precip_results = analyze_precipitation(df)
            season_results = analyze_seasons(df)
            heat_wave_results = analyze_heat_waves(df)
            
            # Save results to CSV
            temp_results.to_csv(f'data/{station}_temperature_analysis.csv', index=False)
            precip_results.to_csv(f'data/{station}_precipitation_analysis.csv', index=False)
            season_results.to_csv(f'data/{station}_seasonal_analysis.csv', index=False)
            heat_wave_results.to_csv(f'data/{station}_heat_wave_analysis.csv', index=False)
            
        except Exception as e:
            print(f"Error processing station {station}: {str(e)}")

if __name__ == "__main__":
    main() 