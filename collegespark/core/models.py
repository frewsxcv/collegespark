from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username, school, password=None):
        user = self.model(
            email=UserManager.normalize_email(email),
            username=username, school=school)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        print School.objects.all()
        school = School.objects.filter(id=1)[0]
        user   = self.create_user(
            email, username=username, school=school, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email      = models.EmailField(unique=True, max_length=255, blank=False, db_index=True)
    username   = models.CharField(max_length=30, blank=False, unique=True)
    major      = models.ForeignKey('Major', blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name  = models.CharField(max_length=30, blank=True)
    is_active  = models.BooleanField(default=True)
    is_admin   = models.BooleanField(default=False)
    school     = models.ForeignKey('School')

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def __repr__(self):
        return "<User {}>".format(self.username)


class School(models.Model):
    name       = models.CharField(max_length=40, unique=True, blank=False)
    short_name = models.CharField(max_length=20, unique=True, blank=False)

    def __unicode__(self):
        return ""

    def __repr__(self):
        return "<School '{}'>".format(self.name)


class Major(models.Model):
    name = models.CharField(max_length=40)
