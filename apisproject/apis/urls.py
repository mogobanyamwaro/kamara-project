from django.urls import path
from .views import calculate_distance_view
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', calculate_distance_view),
]
urlpatterns = format_suffix_patterns(urlpatterns)
