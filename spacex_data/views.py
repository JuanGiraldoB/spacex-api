from django.shortcuts import render

from .utils import (
    categorize_launches,
    fetch_spacex_launches,
    convert_unix_to_ymd,
    get_paginated_launches
)

def paginate_launches(request, page_number, active_tab='active'):
    PER_PAGE = 5
    DEFAULT_PAGE = 1

    all_launches = categorize_launches(fetch_spacex_launches())
    convert_unix_to_ymd(all_launches)

    successful_page = DEFAULT_PAGE if active_tab != 'successful' else page_number
    failed_page = DEFAULT_PAGE if active_tab != 'failed' else page_number
    upcoming_page = DEFAULT_PAGE if active_tab != 'upcoming' else page_number

    # Paginate the launches
    page_obj_successful = get_paginated_launches(all_launches['successful'], successful_page, PER_PAGE)
    page_obj_failed = get_paginated_launches(all_launches['failed'], failed_page, PER_PAGE)
    page_obj_upcoming = get_paginated_launches(all_launches['upcoming'], upcoming_page, PER_PAGE)

    context = {
        'successful': {
            'page_obj': page_obj_successful,
            'url': "terms-by-page-successful",
        },
        'failed': {
            'page_obj': page_obj_failed,
            'url': "terms-by-page-failed",
        },
        'upcoming': {
            'page_obj': page_obj_upcoming,
            'url': "terms-by-page-upcoming",
        },
        f'active_{active_tab}_tab': 'active'
    }

    return render(request, 'spacex_data/index.html', context)


def successful_launches(request, page_number):
    return paginate_launches(request, page_number, active_tab='successful')


def failed_launches(request, page_number):
    return paginate_launches(request, page_number, active_tab='failed')


def upcoming_launches(request, page_number):
    return paginate_launches(request, page_number, active_tab='upcoming')
