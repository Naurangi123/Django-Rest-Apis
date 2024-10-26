
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
# from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics

from .permissions import IsAdminOrReadOnly,IsReviewUserOrReadOnly

from watchlist_app.models import WatchList,StreamPlateform,Review
from watchlist_app.api.serializers import WatchlistSerializer,StreamPlateformSerializer,ReviewSerializer



# By using the concreate class generics based view

class ReviewCreate(generics.CreateAPIView):
    serializer_class=ReviewSerializer
    
    permission_classes=[IsReviewUserOrReadOnly]
    
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        pk=self.kwargs.get('pk')
        watchlist=WatchList.objects.get(pk=pk)
        
        review_user=self.request.user
        review_queryset=Review.objects.filter(watchlist=watchlist, review_user=review_user)
        
        if review_queryset.exists():
            raise ValidationError("You have already reviewed this Movie")
        
        if watchlist.number_rating == 0:
            watchlist.avg_rating=serializer.validated_data['rating']
        else:
            watchlist.avg_rating=(watchlist.avg_rating+serializer.validated_data['rating'])/2
            
        watchlist.number_rating+=1
        watchlist.save()
        
        serializer.save(watchlist=watchlist,review_user=review_user)
    
    
class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        pk=self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
    
    
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes=[IsReviewUserOrReadOnly]
    
    

# generic view with mixins in class based methods

# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


# class ReviewList(mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# Class based api view

# class ReviewApiView(APIView):
#     def get(self, request):
#         review=Review.objects.all()
#         serializer=ReviewSerializer(review,many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer=ReviewSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
 
class StreamPlateformView(viewsets.ModelViewSet):
    queryset=StreamPlateform.objects.all()
    serializer_class=StreamPlateformSerializer
    permission_classes=[IsAdminOrReadOnly]
 
#  -----------------
# class StreamPlateformView(viewsets.ViewSet):
    # def list(self, request):
    #     queryset=StreamPlateform.objects.all()
    #     serializer=StreamPlateformSerializer(queryset,many=True)
    #     return Response(serializer.data)
    
    # def retrieve(self,request,pk=None):
    #     queryset=StreamPlateform.objects.all()
    #     watchlist=get_object_or_404(queryset,pk=pk)
    #     serializer=StreamPlateformSerializer(watchlist)
    #     return Response(serializer.data)
        
    # def create(self, request):
    #     serializer=StreamPlateformSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors)

class StreamPlateformApiView(APIView):
    permission_classes=[IsAdminOrReadOnly]
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
    permission_classes=[IsAdminOrReadOnly]
    
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
    permission_classes=[IsAdminOrReadOnly]
    
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
    permission_classes=[IsAdminOrReadOnly]
    
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