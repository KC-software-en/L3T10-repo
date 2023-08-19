"""Import the modules for render, HttpResponse and login_required
"""
from django.shortcuts import render
# import HttpResponse
from django.http import HttpResponse
# Import the @login_required decorator
# ref: https://docs.djangoproject.com/en/4.2/topics/auth/default/
from django.contrib.auth.decorators import login_required
#############################################################################

# Create your views here.
# define index function referenced in blog/urls.py
# apply login decorator to each view a user may see only when logged in
# include optional login_url parameter to redirect user to login page
@login_required(login_url='user_auth:login')
def index(request):
    """The view index function displays the home page for Cold Meats.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: The rendered HTTP response object.
    :rtype: str
    """
    # comment out HttpResponse once confirmed the page shows
    #return HttpResponse("<h2>Catalogue</h2>")
    # Create a template for your app that will display the catalogue
    # Render your template and map a URL to it
    return render(request, "cold meats.html")
    