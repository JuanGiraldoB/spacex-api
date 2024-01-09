from django.shortcuts import render
from .utils import (
    categorize_launches,
    fetch_spacex_launches,
    convert_unix_to_ymd
)



def index(request):
    launches = categorize_launches(fetch_spacex_launches())
    convert_unix_to_ymd(launches)
    return render(request, 'spacex_data/index.html', launches)


