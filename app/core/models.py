"""
database models
"""

from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)

class Usermanager(BaseUserManager):
  """manager for users"""
  def create_user(self, email, password=None, **extra_fields):
    """create, save and return the new user"""
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user
    

class User(AbstractBaseUser, PermissionsMixin):
  email= models.EmailField(max_length=255, unique=True)
  name= models.CharField(max_length=255)
  is_active= models.BooleanField(default=True)
  is_staff= models.BooleanField(default=False)
  
  objects = Usermanager()
  
  # field we use for authentication
  USERNAME_FIELD = 'email'
   
