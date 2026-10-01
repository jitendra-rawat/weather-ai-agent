from typing import Dict, Any
from langchain_core.tools import tool


CITY_DATABASE: Dict[str, Dict[str, Any]] = {
    "london": {
        "weather": "15°C, Rainy",
        "population": "8.9 million",
        "famous_for": "Big Ben, London Eye, Tower Bridge",
        "timezone": "GMT (UTC+0)"
    },
    "tokyo": {
        "weather": "22°C, Sunny",
        "population": "13.9 million",
        "famous_for": "Tokyo Tower, Shibuya Crossing, Mount Fuji views",
        "timezone": "JST (UTC+9)"
    },
    "new york": {
        "weather": "18°C, Partly Cloudy",
        "population": "8.4 million",
        "famous_for": "Statue of Liberty, Central Park, Times Square",
        "timezone": "EST (UTC-5)"
    },
    "paris": {
        "weather": "17°C, Clear",
        "population": "2.1 million",
        "famous_for": "Eiffel Tower, Louvre Museum, Notre-Dame",
        "timezone": "CET (UTC+1)"
    }
}

@tool
def get_city_weather(city: str) -> str:
    """Fetch current weather data for a given city."""
    key = city.strip().lower()
    data = CITY_DATABASE.get(key)
    if data:
        return f"The current weather in {city.title()} is {data['weather']}."
    return f"Weather data for '{city}' is currently unavailable in the static database."

@tool
def get_city_info(city: str) -> str:
    """Fetch static overview information (population, landmark, timezone) for a given city."""
    key = city.strip().lower()
    data = CITY_DATABASE.get(key)
    if data:
        return (
            f"City Information for {city.title()}:\n"
            f"- Population: {data['population']}\n"
            f"- Famous For: {data['famous_for']}\n"
            f"- Timezone: {data['timezone']}"
        )
    return f"Information for '{city}' was not found in the static database."

# Register all tools into a consumable array
tools = [get_city_weather, get_city_info]