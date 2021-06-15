
from django.urls import include, path
from . views import *
from rest_framework import renderers

otp_send = MobileOtpViewSet.as_view({
    # 'get': 'list',
    'post': 'create'
})
otp_verify = VerifyOtpViewSet.as_view({
    'get':'list'
})

resend_otp = ResendOtpViewSet.as_view({
    'post':'create'
})

urlpatterns = [
    path('send-otp/', otp_send, name='otp_send'),
    path('otp-verify',otp_verify,name='otp_verify'),
    path('resend-otp', resend_otp, name='resend_otp')
    
]

