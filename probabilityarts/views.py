from django.views.generic.base import View
from django.shortcuts import render
from django.contrib.auth.models import User
import json
from django.http import JsonResponse
from utils.probabilityArtist import createImage
from PIL import Image

def index(request):
    return render(request, "probabilityarts/index.html")
         
def create_art(request):
    n = request.POST["n"]
    distribution = request.POST["distribution"]
    baseImage = request.POST["baseImage"]
    image = createImage(n, baseImage, distribution)
    
    image.save('./storefront/static/createdArt/created.jpg')

    print(n, distribution, baseImage)
    return render(request, "probabilityarts/create_art.html", {"n":n,"distribution":distribution, "baseImage":baseImage })
 
 

# if not str(distribution):
        #     return JsonResponse({"distribution_error": "xxx"})