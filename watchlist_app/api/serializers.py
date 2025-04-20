from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Review
        # not want to enter watchlist num while creating review
        exclude = ('watchlist',) 
        # fields = "__all__"
        
class WatchListSerializer(serializers.ModelSerializer):
    # commenting below so that review can't be seen in watchlist
    # to understand pagination
    # reviews = ReviewSerializer(many=True, read_only=True)
    platform = serializers.CharField(source='platform.name')    
    
    class Meta:
        model = WatchList
        fields = "__all__"

class StreamPlatformSerializer(serializers.ModelSerializer):
    # 'watchlist' -> related_name param in 
    # 'platform' field of WatchList model
    watchlist = WatchListSerializer(many=True, read_only=True)
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"    
