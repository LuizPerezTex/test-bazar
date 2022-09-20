from django.urls import path

from .views import (EventsListView, EventsDetailSlugView,)

urlpatterns = [
    path('', EventsListView.as_view()),
    path('<slug:slug>/', EventsDetailSlugView.as_view(), name='detail')

]