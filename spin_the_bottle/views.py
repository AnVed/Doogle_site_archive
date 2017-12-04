from django.shortcuts import render, redirect
import random
import cgi
import html

def start(request):
    return render(request, "index1.html")

def search(request):
    return render(request, "search.html")