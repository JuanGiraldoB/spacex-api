import requests
from datetime import datetime
from django.core.paginator import Paginator

def fetch_spacex_launches():
    url = "https://api.spacexdata.com/v5/launches"
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


def get_paginated_launches(launch, page_number, per_page):
    paginator = Paginator(launch, per_page=per_page)  # Set the number of items per page
    page_obj = paginator.get_page(page_number)  # Get the requested page number
    page_obj.adjusted_elided_pages = paginator.get_elided_page_range(page_number, on_each_side=1, on_ends=1)

    return page_obj

def convert_unix_to_ymd(launches):
    for launch in launches.values():
        for launch_detail in launch:
            launch_detail['date_unix'] = datetime.utcfromtimestamp(launch_detail['date_unix'])