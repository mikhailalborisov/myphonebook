"""myphonebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path


from myphonebookapp.views import (
    PhoneBookListView,
    PhoneBookDetailView,
    PhoneBookCreateView,
    PhoneBookDeleteView,
    PhoneBookUpdateView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("phonebook", PhoneBookListView.as_view(), name="phonebook-list"),
    path("phonebook/add", PhoneBookCreateView.as_view(), name="phonebook-add"),
    path("phonebook/<int:pk>", PhoneBookDetailView.as_view(), name="phonebook-detail"),
    path("phonebook/<int:pk>/delete", PhoneBookDeleteView.as_view(), name="phonebook-delete"),
    path("phonebook/<int:pk>/update", PhoneBookUpdateView.as_view(), name="phonebook-update"),
]