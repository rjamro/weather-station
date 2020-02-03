from django.shortcuts import render

def get_home(request):
    template_name = "home.html"
    return render(request, template_name)