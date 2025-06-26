```markdown
# Aigeon AI - Find Place to Live

## Project Description

Aigeon AI's "Find Place to Live" is a Python-based server application designed to help users discover and gather information about potential places to live. By leveraging external APIs, this application provides detailed data about cities, neighborhoods, towns, and zip codes, assisting users in making informed decisions about their next place to reside.

## Features Overview

- **Location Search**: Search for towns or neighborhoods and retrieve relevant data.
- **Place Information Retrieval**: Obtain detailed information about a specific city or neighborhood based on user input.
- **API Integration**: Utilizes external APIs to fetch up-to-date and accurate information.

## Main Features and Functionality

1. **Location Search Functionality**: 
   - The application allows users to search for locations using a query string. This feature is essential for identifying potential places of interest and obtaining a unique identifier (`urlFragment`) for further data retrieval.

2. **Place Information Retrieval**:
   - Users can retrieve comprehensive data about a specific place by providing the place's identifier and type. This feature is crucial for obtaining detailed insights into the living conditions, amenities, and other relevant aspects of a location.

3. **Integration with External APIs**:
   - The application seamlessly integrates with external APIs to ensure that the information provided is current and reliable. This integration is managed through secure HTTP requests.

## Main Functions Description

### `places_to_live`

- **Description**: Retrieves data about a city or a neighborhood.
- **Parameters**:
  - `place`: A string annotated with a description indicating it should be the `urlFragment` obtained from the location search results.
  - `type`: A string annotated with a description specifying the type of place, which can be "City", "Neighborhood", "Town", or "Zipcode".
- **Returns**: A dictionary containing the data about the specified place.

### `location`

- **Description**: Searches for a town or neighborhood and provides the `urlFragment` value necessary for further data retrieval.
- **Parameters**:
  - `query`: A string annotated with a description used to search for the desired location.
- **Returns**: A dictionary containing search results, including the `urlFragment` for each location found.

This application is designed to be run as a server, utilizing the `FastMCP` framework for handling requests and responses efficiently. By focusing on providing accurate and detailed information, Aigeon AI's "Find Place to Live" serves as a valuable tool for anyone looking to explore new living opportunities.
```