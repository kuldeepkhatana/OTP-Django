from django.db.models import query
from django.shortcuts import render

# Create your views here.
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from . models import *
from . serializers import *

class MobileOtpViewSet(viewsets.ModelViewSet):
    queryset = MobileOtp.objects.all()
    serializer_class = OtpSendSerializer
    
class VerifyOtpViewSet(viewsets.ModelViewSet):
    queryset = MobileOtp.objects.all()
    serializer_class = OtpSendSerializer
    
    
    def get_queryset(self):
        queryset = MobileOtp.objects.all()
        phone = self.request.query_params.get('phone', None)
        otp = self.request.query_params.get('otp', None)
        if phone and otp:
            try:
                verify = MobileOtp.objects.filter(phone=phone,otp=otp)[0]
                if verify:
                    verify.is_verified = True
                    verify.save()
                else:
                    not_verify = MobileOtp.objects.get(phone=phone)
                    not_verify.is_verified = False
                    not_verify.save()
                    
            except:
                pass
        return queryset
    

class ResendOtpViewSet(viewsets.ModelViewSet):
    queryset = MobileOtp.objects.all()
    serializer_class = ResendOtpSerializer
            
            
        
