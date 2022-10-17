from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from myphonebookapp.models import PhoneBook


class PhoneBookListView(generic.ListView):
    model = PhoneBook


class PhoneBookDetailView(generic.DetailView):
    model = PhoneBook


class PhoneBookCreateView(generic.CreateView):
    model = PhoneBook
    fields = ["first_name", "last_name","note","phone","favourites","date_of_creation"]


class PhoneBookDeleteView(generic.DeleteView):
    model = PhoneBook
    success_url = reverse_lazy("phonebook-list")


class PhoneBookUpdateView(generic.UpdateView):
    model = PhoneBook
    fields = ["favourites"]
    template_name_suffix = "_update_form"