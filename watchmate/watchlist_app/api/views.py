from django.shortcuts import render
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerialzer


# Class based api view

class MovieListApiView(APIView):
    def get(self, request):
        movies=Movie.objects.all()
        serializer=MovieSerialzer(movies,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=MovieSerialzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class MovieDetailApiView(APIView):
    def get(self,request,pk):
        try:
            movie=Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'error':"Movie not found"},status=status.HTTP_404_NOT_FOUND)
        serializer=MovieSerialzer(movie)
        return Response(serializer.data)
    
    def put(self,request,pk):
        movie=Movie.objects.get(pk=pk)
        serializer=MovieSerialzer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self,request,pk):
        movie=Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_200_OK)
        

        


# Function based api view

# Create your views here.
# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method=='GET':
#         movies=Movie.objects.all()
#         serializer=MovieSerialzer(movies,many=True)
#         return Response(serializer.data)
    
#     if request.method=='POST':
#         serializer=MovieSerialzer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors) 

# @api_view(['GET','PUT','DELETE'])
# def movie_details(request,pk):
#     if request.method=='GET':
#         try:
#             movie=Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error':"Movie not found"},status=status.HTTP_404_NOT_FOUND)
#         serializer=MovieSerialzer(movie)
#         return Response(serializer.data)
    
#     if request.method=='PUT':
#         movie=Movie.objects.get(pk=pk)
#         serializer=MovieSerialzer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
        
        
#     if request.method=='DELETE':
#         movie=Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_200_OK)