from rest_framework import serializers
from company.models import company_model, watchlist_model
from django.contrib.auth.models import User


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    company_name = serializers.CharField()
    symbol = serializers.CharField(max_length=200)
    scripcode = serializers.IntegerField()

    def create(self, validated_data):
        return company_model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.symbol = validated_data.get('symbol', instance.symbol)
        instance.scripcode = validated_data.get('scripcode', instance.scripcode)
        instance.save()
        return instance




class WatchlistSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    company = serializers.PrimaryKeyRelatedField(queryset=company_model.objects.all())

    def create(self, validated_data):
        return watchlist_model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.company = validated_data.get('company', instance.company)
        instance.save()
        return instance