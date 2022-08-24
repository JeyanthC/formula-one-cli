import json
import requests

def get_current_race_data():
    ''' Method to call Ergast API to fetch the current season race calendar and store it in a file'''

    race_calendar_url = "http://ergast.com/api/f1/current.json"

    payload={}
    headers = {}

    calendar_response = requests.request("GET", race_calendar_url, headers=headers, data=payload)

    response_data = calendar_response.json()

    with open("current_calendar.json", "w") as outfile:
        json.dump(response_data, outfile)