from django.shortcuts import render
from datetime import datetime
import requests


def index(request):
    launches = categorize_launches(fetch_spacex_launches())
    convert_unix_to_ymd(launches)
    return render(request, 'spacex_data/index.html', launches)


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
        for l in launch:
            l['date_unix'] = datetime.utcfromtimestamp(l['date_unix'])