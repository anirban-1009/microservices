from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser
from User.managers import UserManager

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, db_index=True)
    last_name = models.CharField(max_length=50, db_index=True)
    phone = models.CharField(max_length=32, blank = True, validators=[MinLengthValidator(10)])
    email = models.EmailField(max_length=64, db_index=True, unique=True)
    last_login = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    password = models.CharField(max_length=140, default='password@123')
    preferred_language = models.CharField(max_length=20, blank=True, choices=[("en", "English"), ("fr", "French"), ("es", "Spanish")], default="en")
    receive_notifications = models.BooleanField(default=True)
    REQUIRED_FIELDS = ["phone"]
    USERNAME_FIELD = "email"
    objects = UserManager()
    

    class Meta:
        db_table = "models_mgmt_user"

    def __str__(self) -> str:
        return self.email

# Before creating superuser for the first time the foreign key in the database shall be populated with initial data,
# otherwise the user cannot be created. And for initial migration the line `django.contrib.admin,` and `path('admin/', admin.site.urls),`
# from the INSTALLED_APPS and root urls .py shall be commented then migrated, then the lines shall be uncommented.