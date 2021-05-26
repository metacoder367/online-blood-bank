from django.urls import path
from .views import (
    home_page,
    search_page,
    submit_request,
    user_page
)

urlpatterns = [
    path('', home_page, name='home_page'),
    path('search/', search_page, name='search_page'),
    path('user/<int:id>/', user_page, name='user_page'),
    path('submit-request/', submit_request, name='submit_request')
]