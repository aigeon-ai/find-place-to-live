import requests
from datetime import datetime
from typing import Union
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/apimaker/api/find-places-to-live'

mcp = FastMCP('find-places-to-live')

@mcp.tool()
def places_to_live(place: Annotated[str, Field(description='Use urlFragment from /location results.')],
                   type: Annotated[str, Field(description='Valid value: City, Neighboorhood, Town, Zipcode')]) -> dict:
    '''Get data about a city or a neighborhood.'''
    url = 'https://find-places-to-live.p.rapidapi.com/placesToLive'
    headers = {'x-rapidapi-host': 'find-places-to-live.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'place': place,
        'type': type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def location(query: Annotated[str, Field(description='')]) -> dict:
    '''Search for a town or neighborhood. Here you can get `urlFragment` value.'''
    url = 'https://find-places-to-live.p.rapidapi.com/location'
    headers = {'x-rapidapi-host': 'find-places-to-live.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()


if __name__ == "__main__":
    mcp.run(transport="stdio")