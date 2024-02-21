from django.urls import path
from .views import (
    successful_launches,
    failed_launches,
    upcoming_launches
)


urlpatterns = [
    path('successful/<int:page_number>', successful_launches,
         name='terms-by-page-successful'),
    path('failed/<int:page_number>', failed_launches,
         name='terms-by-page-failed'),
    path('upcoming/<int:page_number>', upcoming_launches,
         name='terms-by-page-upcoming')
]
