from rest_framework import serializers
from .models import *

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoGallery
        fields = '__all__'