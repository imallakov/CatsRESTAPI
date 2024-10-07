from rest_framework import serializers
from .models import Cats, Breeds, Ratings
from django.db.models import Avg


class BreedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breeds
        fields = ['id', 'name']


class CatsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    breed_name = serializers.CharField(source='breed.name', read_only=True)
    average_rating = serializers.SerializerMethodField()
    user_rating = serializers.SerializerMethodField()

    class Meta:
        model = Cats
        fields = ['id', 'name', 'age', 'breed', 'breed_name', 'color', 'description', 'user', 'average_rating',
                  'user_rating']

    def get_average_rating(self, obj):
        avg_rating = Ratings.objects.filter(cat=obj).aggregate(Avg('rating'))['rating__avg']
        return avg_rating if avg_rating is not None else 0

    def get_user_rating(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated:
            rating = Ratings.objects.filter(cat=obj, user=user).first()
            return rating.rating if rating else None
        return None


class RatingsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Ratings
        fields = ['user', 'cat', 'rating']
        extra_kwargs = {'cat': {'read_only': True}}

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value
