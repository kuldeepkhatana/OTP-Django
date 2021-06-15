from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy as _, gettext_lazy as _
from django.utils import timezone

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager



# Register you models here
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


GENDER = (
    ('1','Male'),
    ('2','Female'),
    ('3','Other'),
    ('4','--')
)

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.DO_NOTHING)
    date_of_birth = models.DateTimeField(null=True,blank=True)
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    adhar_card = models.CharField(max_length=15,null=True,blank=True)
    social_id = models.CharField(max_length=250,null=True,blank=True)
    status = models.TextField(max_length=500,null=True,blank=True)
    is_verified=models.BooleanField(default=False)
    gender = models.IntegerField(choices=GENDER,default='4')
    class Meta:
        db_table = 'UserProfile'
    
    def __str__(self):
        return str(self.user)
    
class MobileOtp(models.Model):
    # email = models.EmailField()
    phone = models.CharField(max_length=10)
    otp = models.IntegerField(null=True, blank=True)
    otp_time = models.DateTimeField(default=timezone.now)
    otp_expired = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    class Meta:
        db_table = 'MobileOtp'
        
    def __str__(self):
        return self.phone
    
    # @classmethod
    # def verifyOtp(cls, phone, otp):
    #     try:
    #         otp_data = cls.objects.get(phone=phone, otp=otp, is_verified= False)
    #         return otp_data
    #     except:
    #         return False
    
    # @classmethod
    # def latestOtpBymobile(cls, email):
    #     otp_data = cls.objects.filter(phone=phone).order_by('-id')
    #     if otp_data:
    #         try:
    #             return otp_data[0]
    #         except:
    #             return False
    #     else:
    #         return False