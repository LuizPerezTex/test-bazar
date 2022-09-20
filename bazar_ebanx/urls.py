"""bazar_ebanx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from events.views import EventsDetailView, events_detail_view, events_list_view, EventsListView

from events.views import EventsListView, events_list_view, EventsDetailView, events_detail_view, EventsDetailSlugView ,EventsFeaturedListView, EventsFeaturedDetailView
from .views import home_page, about_page, login_page, register_page

urlpatterns = [
        path('', home_page),
        path('about/', about_page),
        path('login/', login_page),
        path('register/', register_page),
        path('featured/', EventsFeaturedListView.as_view()),
        path('featured/<int:pk>/', EventsFeaturedDetailView.as_view()),
        path('events/', EventsListView.as_view()),
        path('events-fbv/', events_list_view),
        path('events/<int:pk>', EventsDetailView.as_view()),
        path('events-fbv/<int:pk>', events_detail_view), 
        path('events/<slug:slug>/', EventsDetailSlugView.as_view()),
        path('events/', include("events.urls")),
        path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)