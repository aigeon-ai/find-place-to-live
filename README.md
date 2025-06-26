```markdown
# Aigeon AI: Find Place to Live

Aigeon AI's `find-place-to-live` is a Python-based server application designed to help users search for and retrieve information about cities, neighborhoods, towns, or zip codes. This application leverages the RapidAPI service to provide detailed data about various locations, making it a valuable tool for individuals or businesses looking to gather insights on potential places to live.

## Features Overview

- **Location Search**: The application allows users to search for towns or neighborhoods using a query string. This feature helps users obtain a `urlFragment`, which is essential for further data retrieval.
- **Place Information Retrieval**: Users can obtain detailed data about specific places, including cities, neighborhoods, towns, or zip codes, by utilizing the `urlFragment` obtained from the location search.

## Main Features and Functionality

The application is built using the FastMCP framework, which facilitates the creation of microservices. It provides two main tools:

1. **Location Search Tool**: This tool enables users to search for a location by name. It returns a dictionary containing relevant information about the location, including the `urlFragment` needed for further queries.

2. **Places to Live Tool**: This tool retrieves detailed information about a specified place. Users can specify the type of place they are interested in (e.g., City, Neighborhood, Town, Zipcode) and obtain comprehensive data about it.

## API Endpoints or Main Functions Description

The application exposes two primary functions, each serving a distinct purpose:

### `location(query: str) -> dict`

- **Description**: Searches for a town or neighborhood based on the provided query string. This function is essential for obtaining the `urlFragment`, which is required for detailed place information retrieval.
- **Parameters**:
  - `query`: A string representing the name or partial name of the location to search for.
- **Returns**: A dictionary containing search results, including the `urlFragment`.

### `places_to_live(place: str, type: str) -> dict`

- **Description**: Retrieves detailed data about a specified place. The function uses the `urlFragment` obtained from the `location` function to fetch information.
- **Parameters**:
  - `place`: A string representing the `urlFragment` of the location.
  - `type`: A string specifying the type of place (valid values: City, Neighborhood, Town, Zipcode).
- **Returns**: A dictionary containing detailed information about the specified place.

Both functions interact with the RapidAPI service to fetch data, utilizing HTTP GET requests with appropriate headers and parameters. The application handles responses by checking the status code and returning the JSON data if the request is successful.

This server application is designed to run using the FastMCP framework's standard input/output transport mechanism, making it suitable for integration into larger systems or for standalone use.

For more information on the API service used, visit the [RapidAPI Find Places to Live](https://rapidapi.com/apimaker/api/find-places-to-live) page.
```
