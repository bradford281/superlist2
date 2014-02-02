from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class ListUserManager(BaseUserManager):
    
    def create_user(self, email):
        ListUser.objects.create(email=email)
    
    def create_superuser(self, email, password):
        self.create_user(email)

class ListUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(primary_key=True)
    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['email', 'height']

    objects = ListUserManager()

    @property
    def is_staff(self):
        return self.email == 'bradford.wade@example.com'

    @property
    def is_active(self):
        return True
    
    
