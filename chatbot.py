"""
    This line imports all functions from the yelpData module.
"""
from yelp_data import get_restaurants, get_sights


def chatbot():
    """
    This function initiates the chatbot, gives an introduction, and processes user input.
    The chatbot can provide restaurant recommendations or sight suggestions based on user input.

    The chatbot continues to run in a loop until the user types 'quit'.
    """

    print(
        "Chatbot: Hi, nice to meet you! My name is Waterloo Mini-Chatbot! I can recommend "
        "restaurants or places to visit in Waterloo.\n"
        "Type 'restaurants' to get a list of all the great restaurants in the area\n"
        "or 'sights' to get a list of all the amazing places to visit in Waterloo.\n"
        "If you want to exit, you just have to type 'quit'."
    )

    while True:
        # Accepting user input in lowercase to make it case-insensitive.
        user_input = input("\nYou: ").lower()

        if user_input == "quit":
            print("\nChatbot: Goodbye! Hope to see you soon!")
            break  # Exit the chatbot loop if the user types 'quit'.

        # Check if the user is asking for restaurant recommendations.
        if "restaurant" in user_input:
            print("\nChatbot: Fetching top restaurants in Waterloo... ")
            # Fetch restaurants using the Yelp API function.
            restaurants = get_restaurants()

            if restaurants:
                print("\nChatbot: Here are some recommendations: ")
                for restaurant in restaurants:
                    print(
                        f"- {restaurant['name']} (Rating: {restaurant['rating']})")
                    print(f"  Address: {restaurant['address']}")
                    print(f"  Phone: {restaurant['phone']}")

            else:
                print("\nChatbot: Sorry, I couldn't find any restaurants in the area.")

        if "sights" in user_input:
            print("\nChatbot: Fetching top sights in Waterloo... ")
            # Fetch sights using the Yelp API function.
            sights = get_sights()

            if sights:
                print("\nChatbot: Here are some amazing places to visit: ")
                for sight in sights:
                    print(f"- {sight['name']} (Rating: {sight['rating']})")
                    print(f"  Address: {sight['address']}")
                    print(f"  Phone: {sight['phone']}")
            else:
                print("\nChatbot: Sorry, I couldn't find any sights in the area.")

        else:
            print(
                "\nChatbot: Sorry, I can only help with 'restaurants' and 'sights' at the moment.")


if __name__ == "__main__":
    chatbot()
