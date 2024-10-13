from django.shortcuts import render
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from watchlist_app.models import WatchList,StreamPlateform
from watchlist_app.api.serializers import WatchlistSerializer,StreamPlateformSerializer


# Class based api view


class StreamPlateformApiView(APIView):
    def get(self, request):
        plateform=StreamPlateform.objects.all()
        serializer=StreamPlateformSerializer(plateform,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=StreamPlateformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class StreamDetailApiView(APIView):
    def get(self,request,pk):
        try:
            platefromone=StreamPlateform.objects.get(pk=pk)
        except StreamPlateform.DoesNotExist:
            return Response({'error':"Not found"},status=status.HTTP_404_NOT_FOUND)
        serializer=StreamPlateformSerializer(platefromone)
        return Response(serializer.data)
    
    def put(self,request,pk):
        plateformone=StreamPlateform.objects.get(pk=pk)
        serializer=StreamPlateformSerializer(plateformone,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self,request,pk):
        plateformone=StreamPlateform.objects.get(pk=pk)
        plateformone.delete()
        return Response(status=status.HTTP_200_OK)



class WatchListApiView(APIView):
    def get(self, request):
        watchlists=WatchList.objects.all()
        serializer=WatchlistSerializer(watchlists,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class WatchDetailApiView(APIView):
    def get(self,request,pk):
        try:
            watchlistone=WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error':"Not found"},status=status.HTTP_404_NOT_FOUND)
        serializer=WatchlistSerializer(watchlistone)
        return Response(serializer.data)
    
    def put(self,request,pk):
        watchlistone=WatchList.objects.get(pk=pk)
        serializer=WatchlistSerializer(watchlistone,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self,request,pk):
        watchlistone=WatchList.objects.get(pk=pk)
        watchlistone.delete()
        return Response(status=status.HTTP_200_OK)
        
        



# Function based api view

# Create your views here.
# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method=='GET':
#         movies=WatchListApiView.objects.all()
#         serializer=MovieSerializer(movies,many=True)
#         return Response(serializer.data)
    
#     if request.method=='POST':
#         serializer=MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors) 

# @api_view(['GET','PUT','DELETE'])
# def movie_details(request,pk):
#     if request.method=='GET':
#         try:
#             movie=WatchListApiView.objects.get(pk=pk)
#         except WatchListApiView.DoesNotExist:
#             return Response({'error':"WatchListApiView not found"},status=status.HTTP_404_NOT_FOUND)
#         serializer=MovieSerializer(movie)
#         return Response(serializer.data)
    
#     if request.method=='PUT':
#         movie=WatchListApiView.objects.get(pk=pk)
#         serializer=MovieSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
        
        
#     if request.method=='DELETE':
#         movie=WatchListApiView.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_200_OK)