from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlateform
from django.utils.timezone import now




# By ModelSerializer

class WatchlistSerializer(serializers.ModelSerializer):    
    class Meta:
        model=WatchList
        fields="__all__"
        
        
               
class StreamPlateformSerializer(serializers.ModelSerializer):
    watchlist=WatchlistSerializer(many=True,read_only=True)
    
    # for only string fields
    # watchlist=serializers.StringRelatedField(many=True)
    
    #via Hyperlinke
    # watchlist=serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='movie')
    
    #Via Key 
    # watchlist=serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model=StreamPlateform
        fields="__all__"
        
        # fields=['id', 'name', 'description']
        # exclude=['name']
    
    # ------------------ These for checking validation --------------------------------
    # def get_len_names(self,object):
    #     return len(object.name)
    
    # #Object level validation
    # def validate(self, data):
    #     if data['name']==data['description']:
    #         raise serializers.ValidationError("Name and Description aren't be same.")
    #     return data
    
    # #Field level validation
    # def validate_name(self,value):
    #     if len(value)<2:
    #         raise serializers.ValidationError("Name is too short.")
    #     else:
    #         return value





# By Serializers 

# #validators
# def check_name(name):
#     if len(name)<2:
#         raise serializers.ValidationError("Name is too short.")
    
    


# class MovieSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField(validators=[check_name])
#     description=serializers.CharField()
#     active=serializers.BooleanField()
    
    
#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.description=validated_data.get('description',instance.description)
#         instance.active=validated_data.get('active',instance.active)
#         instance.save()
#         return instance
    
#     #Object level validation
#     def validate(self, data):
#         if data['name']==data['description']:
#             raise serializers.ValidationError("Name and Description aren't be same.")
#         return data
    
#     #Field level validation
#     # def validate_name(self,value):
#     #     if len(value)<2:
#     #         raise serializers.ValidationError("Name is too short.")
#     #     else:
#     #         return value