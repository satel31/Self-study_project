from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    username = None

    first_name = models.CharField(max_length=235, verbose_name='Name', **NULLABLE)
    last_name = models.CharField(max_length=235, verbose_name='Last name', **NULLABLE)

    email = models.EmailField(unique=True, verbose_name='Email')
    city = models.CharField(max_length=235, verbose_name='City', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Avatar', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Phone', **NULLABLE)
    telegram = models.CharField(max_length=150, verbose_name='Telegram')

    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER, verbose_name='Role')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
