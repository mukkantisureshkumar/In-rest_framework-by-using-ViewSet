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
        po=Product.objects.get(pk=pk)
        jso=Productms(po)
        return Response(jso.data)
    def create(self,request):
        jd=request.data
        pmso=Productms(data=jd)
        if pmso.is_valid():
            pmso.save()
            return Response({'message':'product is creatd'})
        return Response({'fail':'product is not created'})
    def update(self,request,pk):
        po=Product.objects.get(pk=pk)
        jso=Productms(po,data=request.data)
        if jso.is_valid():
            jso.save()
            return Response({'update':'data updated'})
        return Response({'fail':'update is fail'})
    def partial_update(self,request,pk):
        po=Product.objects.get(pk=pk)
        jd=request.data
        jso=Productms(po,jd,partial=True)
        if jso.is_valid():
            jso.save()
            return Response({'partial':'updated data'})
        return Response({'fail':'data failed'})
    def destroy(self,request,pk):
        #Product.objects.get(pk=pk).delete()
        po=Product.objects.get(pk=pk)
        po.delete()
        return Response({'destroy':'deleted the data'})
    