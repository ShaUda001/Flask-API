# Flask-API
Custom API Project with Flask

This is a script in python that has cutom API endpoints using Flask framework and is run locally on localhost port 5000

This project is a Flask-based application that provides multiple API endpoints to retrieve data from free public APIs. The API is hosted on a local Flask server (localhost IP: 127.0.0.1) and outputs data in JSON format. Users can interact with various endpoints to receive real-time data such as the current location of the ISS, random Chuck Norris jokes, Pokémon information, and more.
Features:

Multiple Endpoints:
    /iss/ - Get the current location of the International Space Station.
    /chuck-norris/ - Fetch a random Chuck Norris joke.
    /dog/ - Retrieve a random dog image.
    /breweries/ - Get a list of breweries.
    /pokemon/?pokemon=ENTER_POKEMON_NAME - Fetch data for a specific Pokémon.
    /random-user/ - Generate a random user profile.
    /cat-fact/ - Get a random cat fact.
    /joke/ - Fetch a random joke.
User Input Support:
    The Pokémon endpoint allows users to input a Pokémon name to fetch detailed information.
    Use the endpoint '/pokemon/?pokemon=ENTER_POKEMON_NAME' and replace [ENTER_POKEMON_NAME] with the name of the pokemon
Flask Framework:
    The project is built using Flask, providing a simple yet powerful way to create API routes and handle requests.
JSON Responses:
    All endpoints return data in structured JSON format, making it easy to integrate with other applications or systems.

How to Run:

Clone this repository.
Install the required dependencies (Flask, requests).
Run the Flask server locally using python main.py.
Access the API via http://127.0.0.1:5000/ in your browser or via API testing tools like Postman.
