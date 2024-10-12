# from django.http import JsonResponse
# from django.shortcuts import render
# from .models import Movie

# # Create your views here.

# def movie_list(request):
#     movies=Movie.objects.all()
#     data={
#         'movies':list(movies.values())
#     }
#     return JsonResponse(data)
    
# def movie_details(request,pk):
#     movie=Movie.objects.get(id=pk)
    
#     data={
#         'id':movie.id,
#         'name':movie.name,
#         'description':movie.description,
#         'active':movie.active,
#     }
#     return JsonResponse(data)