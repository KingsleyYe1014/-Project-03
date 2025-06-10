# Climate Data Analysis Project

## Project Description
This project is the third assignment for AAE 718 (Data Science for Agricultural and Applied Economics) course. The project focuses on analyzing climate data from multiple weather stations to study climate change patterns in Wisconsin. We analyze temperature trends, precipitation patterns, and other climate indicators to understand how climate has changed over time in different regions.

## Data Source
The data used in this project comes from the NOAA Global Historical Climatology Network-Daily (GHCN-D) database. Due to the large size of the data files, they are not included in this repository. You can access the data files from the following locations:

- [Download Link (Google Drive)](YOUR_GOOGLE_DRIVE_LINK_HERE)
- Original Source: [NOAA Climate Data](https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/v3.30/)

## Project Structure
```
.
├── .gitignore          # Git ignore configuration
├── README.md           # Project documentation
├── report.md           # Detailed analysis report in markdown format
├── images/            # Generated plots and visualizations
├── climate_analysis.py # Main analysis script
├── download_data.py    # Data download and preprocessing script
└── requirements.txt    # Python dependencies
```

## Setup and Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/KingsleyYe1014/AAE718-Project3.git
   cd AAE718-Project3
   ```

2. Create and activate Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   .\venv\Scripts\activate  # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download the data:
   - Download the CSV files from the Google Drive link provided above
   - Place the files in the `data/` directory

5. Run analysis:
   ```bash
   python climate_analysis.py
   ```

## Analysis Components
1. Temperature Trends Analysis
   - Annual mean temperature changes
   - Seasonal temperature variations
   - Daily temperature extremes

2. Precipitation Analysis
   - Annual precipitation patterns
   - Extreme precipitation events
   - Seasonal distribution

3. Climate Change Indicators
   - Long-term temperature trends
   - Precipitation pattern changes
   - Extreme weather events frequency

## Results
The complete analysis and findings are documented in [report.md](report.md). The visualizations can be found in the `images/` directory.

## Author
Kingsley Ye

## License
MIT License

