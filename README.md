# Climate Data Analysis Project

## Project Description
This project is the third assignment for AAE 718 (Data Science for Agricultural and Applied Economics) course. The project focuses on analyzing climate data from multiple weather stations to study climate change patterns.

## Data Requirements
- Data from at least 4 weather stations
- At least 10 years of data from each station
- Data source: [NOAA Climate Data](https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/v3.30/)

## Project Structure
```
.
├── .gitignore          # Git ignore configuration
├── README.md           # Project documentation
├── report.md           # Analysis report
├── images/             # Generated plots and visualizations
├── data/              # Data files (if size permits)
├── climate_analysis.py # Main analysis script
├── download_data.py    # Data download script
└── requirements.txt    # Python dependencies
```

## Running Instructions
1. Clone this repository:
   ```bash
   git clone https://github.com/KingsleyYe1014/-Project-03.git
   cd -Project-03
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

4. Download data:
   ```bash
   python download_data.py
   ```

5. Run analysis:
   ```bash
   python climate_analysis.py
   ```

## Analysis Components
1. Temperature Trends Analysis
   - Annual mean temperature changes
   - Seasonal temperature variations

2. Precipitation Analysis
   - Annual precipitation patterns
   - Extreme precipitation events

3. Seasonal Analysis
   - Changes in season length
   - Seasonal temperature patterns

4. Heat Wave Analysis
   - Frequency of heat waves
   - Duration and intensity trends

## Results
The complete analysis results can be found in [report.md](report.md). Key findings include:
- Temperature trends across Wisconsin
- Changes in precipitation patterns
- Seasonal variations
- Heat wave frequency analysis

## Author
[KingsleyYe1014]

## License
MIT License
