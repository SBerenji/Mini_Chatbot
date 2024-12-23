"""
    This line imports all the required libraries to call the yelp API 
"""
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the Yelp API key from the environment
API_KEY = os.getenv("YELP_API_KEY")


# Check if the API key is loaded
if not API_KEY:
    raise ValueError(
        "YELP_API_KEY is not set. Make sure it's properly set in the .env file.")

# Set up the API headers
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

# Yelp API endpoint
API_URL = "https://api.yelp.com/v3/businesses/search"


def get_yelp_data(term,  latitude=43.4643, longitude=-80.5204, limit=5):
    """
    Fetches data from Yelp API based on the given parameters.

    Args:
        term (str): The search term (e.g., 'restaurants', 'tourist attractions').
        location (str): The location for the search (default: "Waterloo, ON").
        categories (str): The categories for filtering results (default: None).
        limit (int): The number of results to return (default: 5).

    Returns:
        List of businesses with their details (name, rating, address, phone).
    """

    params = {
        "term": term,
        "latitude": latitude,
        "longitude": longitude,
        "limit": limit
    }

    response = requests.get(API_URL, headers=HEADERS,
                            params=params, timeout=10)     # Timeout set to 10 seconds

    if response.status_code == 200:
        businesses = response.json().get("businesses", [])
        return [
            {
                "name": biz["name"],
                "rating": biz.get("rating", "N/A"),
                "address": ", ".join(biz["location"]["display_address"]),
                "phone": biz.get("phone", "N/A")
            }
            for biz in businesses
        ]

    # This part is not inside else anymore, as it's after the return
    print("Error:", response.status_code, response.text)
    return None


def get_restaurants(limit=5):
    """
    Fetches top restaurants from Yelp API.

    Args:
        location (str): The location for the search (default: "Waterloo, ON").
        limit (int): The number of results to return (default: 5).

    Returns:
        List of restaurants with their details.
    """
    return get_yelp_data("restaurants", limit=limit)


def get_sights(limit=5):
    """
    Fetches tourist sights in Waterloo from Yelp API.

    Args:
        location (str): The location for the search (default: "Waterloo, ON").
        limit (int): The number of results to return (default: 5).

    Returns:
        List of tourist sights with their details.
    """
    return get_yelp_data("tourist attractions", limit=limit)
