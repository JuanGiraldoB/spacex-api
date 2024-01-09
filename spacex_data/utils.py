import requests
from datetime import datetime

def fetch_spacex_launches():
    url = "https://api.spacexdata.com/v4/launches"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return []


def categorize_launches(launches):
    successful = list(
        filter(lambda x: x['success'] and not x['upcoming'], launches))

    failed = list(
        filter(lambda x: not x['success'] and not x['upcoming'], launches))

    upcoming = list(
        filter(lambda x: x['upcoming'], launches))

    return {
        'successful': successful,
        'failed': failed,
        'upcoming': upcoming,
    }


def convert_unix_to_ymd(launches):
    for launch in launches.values():
        for launch_detail in launch:
            launch_detail['date_unix'] = datetime.utcfromtimestamp(launch_detail['date_unix'])