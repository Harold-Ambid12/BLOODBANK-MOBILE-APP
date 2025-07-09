from rest_framework import serializers
from .models import User, Donation, BloodInventory
from django.contrib.auth import get_user_model

from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'password', 'first_name', 'age', 'gender', 'medical_history', 'contact_number', 'address', 'blood_type']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ['id', 'quantity', 'date', 'donor']
        read_only_fields = ['date', 'donor']  # donor will be set in the view

    def create(self, validated_data):
        validated_data['donor'] = self.context['request'].user
        return super().create(validated_data)


class BloodInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodInventory
        fields = '__all__'