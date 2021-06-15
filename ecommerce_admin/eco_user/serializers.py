import math, random
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from . models import *
from .managers import *
class RegUserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    phone = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = CustomUser
        # fields = '__all__'
        exclude = ['is_superuser','is_staff','user_permissions','groups','date_joined','last_login']
        
        
    def create(self, validated_data):
        reg_data = CustomUser.objects.create(**validated_data)
        return reg_data
    

class OtpSendSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(required=True)
    
    class Meta:
        model = MobileOtp
        fields = '__all__'

    def create(self, validated_data):
        """ return overide create """
        otp_data = MobileOtp.objects.create(**validated_data)
        try:
            check_exist = MobileOtp.objects.filter(phone=validated_data['phone'])
            check_exist.delete()
        except MobileOtp.DoesNotExist:
            pass
        otp_data.otp = generateOTP()
        otp_data.save()

        return otp_data   
    
    
class VerifyOtpSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(required=True)
    otp = serializers.IntegerField(required=True)

    class Meta:
        model = MobileOtp
        fields = ['phone','otp','is_verified']
        
    
class ResendOtpSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(required=True)
    
    
    class Meta:
        model = MobileOtp
        fields = '__all__'
        
    def create(self, validated_data):
        """ return overide create """
        try:
            check_exist = MobileOtp.objects.filter(phone=validated_data['phone'])
            check_exist.delete()
        except MobileOtp.DoesNotExist:
            pass
        otp_data = MobileOtp.objects.create(**validated_data)
        otp_data.otp = generateOTP()
        otp_data.save()

        return otp_data  
        
    
        

    
    
