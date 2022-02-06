from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .models import UserProfile
from .forms import ProfileForm


# Create your views here.

class CreateProfileView(CreateView):
    model = UserProfile
    # form_class = ProfileForm
    fields = "__all__"
    template_name = "profiles/create_profile.html"
    success_url = "/profiles"

class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/user_profile.html"
    context_object_name = "profiles"