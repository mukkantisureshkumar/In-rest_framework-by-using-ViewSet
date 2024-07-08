from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet
from app.models import *
from app.serializers import *
from rest_framework.response import Response
class ProductCrudView(ViewSet):
    def list(self,request):
        po=Product.objects.all()
        jso=Productms(po,many=True)
        return Response(jso.data)
    def retrieve(self,request,pk):
        po=Product.objects.get(pid=pk)
        jso=Productms(po)
        return Response(jso.data)
        