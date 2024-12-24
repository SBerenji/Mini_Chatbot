"""
Flask application for a simple chatbot 
"""
from flask import Flask, render_template, request
from yelp_data import get_restaurants, get_sights


app = Flask(__name__)


@app.route("/")
def index():
    """
    Renders the main chat page.
    """
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    """
    Handles the user input from the frontend and returns the chatbot response.
    """

    # Get the user's message from the frontend (sent via POST)
    msg = request.form["msg"]

    # Process the message with the chatbot logic
    response = get_chat_response(msg)

    # Return the response as JSON
    return response


def get_chat_response(text):
    """
    This function processes the user input and returns the appropriate chatbot response.
    It checks if the input contains 'restaurant' or 'sights' and fetches corresponding 
    information from the Yelp API.
    """

    text = text.lower()  # Ensuring that the input is case-insensitive

    if "restaurant" in text:
        restaurants = get_restaurants()
        if restaurants:
            response = "Here are some great restaurants in Waterloo:\n"
            for restaurant in restaurants:
                response += (f"{restaurant['name']} (Rating: {restaurant['rating']}) - "
                             f"{restaurant['address']} - {restaurant['phone']}\n")
        else:
            response = "Sorry, I couldn't find any restaurants in the area."

    elif "sights" in text:
        sights = get_sights()
        if sights:
            response = "Here are some amazing places to visit in Waterloo:\n"
            for sight in sights:
                response += (f"{sight['name']} (Rating: {sight['rating']}) - "
                             f"{sight['address']} - {sight['phone']}\n")
        else:
            response = "Sorry, I couldn't find any sights in the area."

    else:
        response = "I can only help with 'restaurants' and 'sights' at the moment."

    return response


if __name__ == "__main__":
    app.run(debug=True)
