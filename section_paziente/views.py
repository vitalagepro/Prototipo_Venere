from django.shortcuts import render
from django.views import View
import requests


from section_medico.models import Prenotazioni, ApiKeys

class LoginPaziente(View):
    def get(self, request):
        return render(request, "structure/login_paziente.html")
    
    def post(self, request):

        api_key_instance = ApiKeys.objects.get(id=1)
        api_key = api_key_instance.ApiKeys

        url_api_instance = ApiKeys.objects.get(id=1)
        news_api_url = url_api_instance.Api

        params = {
            'apiKey': api_key,  
        }

        response = requests.get(news_api_url, params=params)

        if response.status_code == 200:
            news_data = response.json().get('articles', [])

            return render(request, "structure/HomePagePaziente.html", {'news_data': news_data})

        else:
            print(f"Error: {response.status_code}")
            return render(request, "structure/HomePagePaziente.html")
        
def HomePageRendering(request):
    api_key_instance = ApiKeys.objects.get(id=1)
    api_key = api_key_instance.ApiKeys

    url_api_instance = ApiKeys.objects.get(id=1)
    news_api_url = url_api_instance.Api

    params = {
        'apiKey': api_key,  
    }

    response = requests.get(news_api_url, params=params)

    if response.status_code == 200:
        news_data = response.json().get('articles', [])

        return render(request, "structure/HomePagePaziente.html", {'news_data': news_data})

    else:
        print(f"Error: {response.status_code}")
        return render(request, "structure/HomePagePaziente.html")

def ProfiloPaziente(request):
    return render(request, "structure/includes/profilo.html")