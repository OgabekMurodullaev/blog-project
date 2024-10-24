from django.urls import path

from pages.views import (HomePageView, MostViewedAllTimeView, MostViewedThisWeekView,
                         MostViewedThisMonthView, LatestPostsView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('most-viewed/all-time/', MostViewedAllTimeView.as_view(), name='all-time'),
    path('most-viewed/week/', MostViewedThisWeekView.as_view(), name='weekly'),
    path('most-viewed/month/', MostViewedThisMonthView.as_view(), name='monthly'),
    path('latest/', LatestPostsView.as_view(), name='latest')

]