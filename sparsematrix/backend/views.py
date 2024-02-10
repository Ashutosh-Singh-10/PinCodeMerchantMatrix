from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser

from .models import *
from .serializers import *


from rest_framework.views import APIView
from rest_framework.response import Response

class GetMerchants(APIView):
    def post(self,request):
        if("pinCode" not in request.data):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        query=MerchantOrdered.objects.filter(merchantId=request.data["pinCode"]).values()
        serializer=MerchantOrderedSerializer(query,many=True)
        return Response(serializer.data)    
class GetPin(APIView):
    def post(self,request):
        if("merchantId" not in request.data):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        query=MerchantOrdered.objects.filter(merchantId=request.data["merchantId"]).values()
        serializer=MerchantOrderedSerializer(query,many=True)
        return Response(serializer.data)
        
