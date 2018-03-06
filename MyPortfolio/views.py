from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout, authenticate
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Q
from itertools import chain
from django.db.models import Sum

from django.shortcuts import redirect, render

def home(request):
    return render(request, 'index.html')
