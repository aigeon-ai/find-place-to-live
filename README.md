# Aigeon AI: Find Place to Live

## Project Description

Aigeon AI's "Find Place to Live" is a Python-based server application designed to assist users in discovering and retrieving information about various locations, such as cities, neighborhoods, towns, and zip codes. This application leverages external APIs to provide comprehensive data about potential living areas, making it an invaluable tool for individuals seeking to relocate or explore new environments.

## Features Overview

- **Location Search**: The application allows users to search for towns or neighborhoods and retrieve detailed information about these locations.
- **Place Information Retrieval**: Users can obtain specific data about a city or neighborhood by using a unique identifier obtained from the location search.
- **API Integration**: The application integrates with external APIs to fetch up-to-date and accurate information about different places.

## Main Features and Functionality

1. **Location Search Functionality**: 
   - The application provides a tool to search for a town or neighborhood using a query string. This feature returns relevant data, including a unique `urlFragment` that can be used for further data retrieval.

2. **Place Information Retrieval**:
   - Users can retrieve detailed information about a specific place by providing the `urlFragment` obtained from the location search and specifying the type of place (e.g., City, Neighborhood, Town, Zipcode).

3. **External API Communication**:
   - The application communicates with an external API to ensure that the data provided is current and reliable. This integration is seamless and transparent to the user, offering a smooth user experience.

## Main Functions Description

### `places_to_live`

- **Purpose**: This function retrieves data about a specific city or neighborhood.
- **Parameters**:
  - `place`: A string annotated with a description indicating it should be the `urlFragment` obtained from the location search results.
  - `type`: A string indicating the type of place, which can be "City", "Neighborhood", "Town", or "Zipcode".
- **Returns**: A dictionary containing the data about the specified place. If the request fails, it returns an empty dictionary.
- **Description**: This function constructs a request to the external API with the provided parameters and returns the response in a structured format.

### `location`

- **Purpose**: This function searches for a town or neighborhood based on a query string.
- **Parameters**:
  - `query`: A string representing the search term for the desired location.
- **Returns**: A dictionary containing search results, including the `urlFragment` for each location. If the request fails, it returns an empty dictionary.
- **Description**: This function sends a request to the external API with the search query and processes the response to extract relevant location data.

The application is designed to run as a server, using the `FastMCP` framework to manage communication and processing. This setup ensures efficient handling of requests and responses, providing users with a reliable tool for finding places to live.