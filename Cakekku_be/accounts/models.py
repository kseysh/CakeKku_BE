from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin,Group,Permission
class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, userID, password):

        user = self.model(
            userID = userID
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, userID, password):
        superuser = self.create_user(userID = userID, password = password)
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        superuser.save(using=self._db)
        
        return superuser
    
class User(AbstractBaseUser, PermissionsMixin):
    userID = models.CharField(max_length=50, unique = True)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')

    def is_staff(self):
        return self.is_admin
    
    objects = UserManager()

    USERNAME_FIELD = 'userID'

    class Meta:
        db_table = 'user'