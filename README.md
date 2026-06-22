# Weather API

A Python backend that fetches weather data from the [Visual Crossing API](https://www.visualcrossing.com/weather-api) and serves it via a Flask endpoint, with Redis caching to reduce redundant API calls.
https://roadmap.sh/projects/weather-api-wrapper-service

## How It Works

When a request comes in for a location:
1. The server checks Redis for a cached result
2. If found, it returns the cached data immediately (cache hit)
3. If not found, it calls the Visual Crossing API, caches the result for 15 days, and returns it (cache miss)

## Requirements

- Python 3.x
- [Memurai](https://www.memurai.com/) (Redis-compatible server for Windows) or Redis
- A free [Visual Crossing API key](https://www.visualcrossing.com/weather-api)

## Installation

1. Clone the repository
2. Install dependencies:
```
pip install flask python-dotenv redis requests
```
3. Install and start Memurai (Windows) or Redis
4. Create a `key.env` file in the project root:
```
API_KEY=your_visual_crossing_api_key_here
```

## Usage

Run the Flask server:
```
python Weather_API.py
```

Then make a request to:
```
http://localhost:5000/<location>
```

Where `<location>` can be a city name, address, or coordinates. For example:
```
http://localhost:5000/Lisbon
http://localhost:5000/New York
http://localhost:5000/48.8566,2.3522
```

The response is a JSON object containing weather data for the requested location.

## Environment Variables

| Variable | Description |
|----------|-------------|
| `API_KEY` | Your Visual Crossing API key |

## Error Handling

| Scenario | Response |
|----------|----------|
| Redis unavailable | `500` - Could not connect to Redis |
| Invalid location / API error | `502` - API error with status code |
| No internet connection | `503` - No internet connection |

## Project Structure

```
Weather_API/
├── Weather_API.py   # Main application
├── key.env          # Environment variables (not tracked by Git)
└── .gitignore
```
