# Weather.com Scraper

A simple Python script that scrapes current weather information from weather.com for multiple locations.

## Features

- Fetches current weather conditions including temperature, feels-like temperature, and weather phrase
- Displays sunrise and sunset times
- Shows detailed weather metrics (high/low, wind, humidity, pressure)
- Includes Air Quality Index (AQI) information
- Supports multiple locations from a text file
- Automatically creates `locations.txt` if it doesn't exist

## Requirements

- Python 3.x
- BeautifulSoup4
- Requests
- lxml

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/weather-scraper.git
cd weather-scraper
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

## Setup

The script will automatically create a `locations.txt` file if it doesn't exist. To add your locations:

1. Get your location ID from weather.com:

   - Visit [weather.com](https://weather.com)
   - Search for your city
   - Copy the 64-character location ID from the URL
   - URL format: `https://weather.com/en-IN/weather/today/l/[LOCATION-ID]`
   - Example: `https://weather.com/en-IN/weather/today/l/a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6`

2. Open `locations.txt` and add location IDs (one per line):

```
a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6
b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6a1
```

## Usage

Run the script:

```bash
python main.py
```

## Output Example

```
New York, NY
As per 2:30 PM IST
72°F [Partly Cloudy]

Feels Like : 70°F
Sun Rise : 6:45 AM
Sun Set : 7:30 PM
High/Low : 75°/65°
Wind : NE 8 mph
Humidity : 65%
Pressure : 30.12 in

AQI : 45 [Good]
Air quality is satisfactory, and air pollution poses little or no risk.
```

## File Structure

```
weather-scraper/
│
├── main.py              # Main script
├── locations.txt        # Location IDs (auto-created if missing)
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Requirements.txt Contents

```
beautifulsoup4
requests
lxml
```

## Important Notes

- This script scrapes data from weather.com. Be aware that:
  - HTML structure may change, breaking the script
  - Consider using an official weather API for production applications
- The script uses specific CSS classes that may change over time
- Rate limiting: Avoid making too many requests in a short period

## Troubleshooting

**"No locations found" or empty output:**

- Open `locations.txt` and add valid location IDs
- Ensure each ID is on a separate line

**AttributeError: 'NoneType' object has no attribute 'text'**

- The HTML structure of weather.com has changed
- The location ID may be invalid
- Check your internet connection

**No data displayed:**

- Verify your location ID is correct
- Ensure `locations.txt` contains valid IDs

## Disclaimer

This project is for educational purposes only. Always respect website Terms of Service and robots.txt. For production applications, consider using official weather APIs such as:

- OpenWeatherMap API
- WeatherAPI
