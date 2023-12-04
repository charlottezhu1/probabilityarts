from django.shortcuts import render
from django.contrib.auth.models import User
import json
from django.http import JsonResponse

# Create your views here.
# def index(request):
#         return render(request, "probabilityarts/index.html")
    
# class createArtView(View):

# def post(self, request):
def index(request):
    # data = json.loads(request.body)
    # print(data)
    # n = data["n"]
    # distribution = data("distribution")
    
    return render(request, "probabilityarts/index.html")
        
        # if not str(distribution):
        #     return JsonResponse({"distribution_error": "xxx"})
        


def create_art(request):
    return render(request, "probabilityarts/create_art.html")

