from django.shortcuts import render
from rest_framework.views import APIView
#from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import ClienteCobranca
# Create your views here.

class ClienteCobrancaList(APIView):
    def post(self,request):
        ClienteCobranca.objects.create(
            name=request.data["name"],
            cpf = request.data["cpf"],
            email = request.data["email"],
            phone_number = request.data["phone_number"],
            street = request.data["street"],
            neighborhood = request.data["neighborhood"],
            zipcode = request.data["zipcode"],
            city = request.data["city"],
            complement = request.data["complement"],
            state = request.data["state"],
            value = request.data["value"],
            expire_at = request.data["expire_at"],
            sigla = request.data["sigla"]
        )

        return JsonResponse({'success': True})