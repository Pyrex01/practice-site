from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,phone_no,date_of_birth,gender,email,password=None):
        if not last_name:
            raise ValueError("Users must have last name")
        if not first_name:
            raise ValueError("Users must have first name")
        if not date_of_birth:
            raise ValueError("Users must be valid")
        if not gender:
            raise ValueError("Users must belong to one categorie")
        if not phone_no:
            raise ValueError("Users must have phone number")

        user = self.model(
            email=self.normalize_email(email),
            last_name=self.model.normalize_username(last_name),
            first_name=self.model.normalize_username(first_name),
            date_of_birth=date_of_birth,
            gender=gender,
            phone_no=phone_no
        )
        user.set_password(password)
        user.save(using=self.db)
        return user


    def create_superuser(self,first_name,last_name,phone_no,date_of_birth,gender,password=None):
        user = self.model(
            last_name=self.model.normalize_username(last_name),
            first_name=self.model.normalize_username(first_name),
            date_of_birth=date_of_birth,
            gender=gender,
            phone_no=phone_no
        )
        user.is_admin=True
        user.is_verify=True
        user.set_password(password)
        user.save(using=self.db)
        return user


class Accounts(AbstractBaseUser):
    #User data
    email = models.EmailField(max_length=60,default='')
    phone_no = models.CharField(max_length=255,unique=True,blank=False,null=False)
    date_of_birth = models.DateField()
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others','Others')
    )
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES)

    #time date entries
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login",auto_now=True)
    #permisisons here
    is_admin = models.BooleanField(default=False)
    #  loggers
    USERNAME_FIELD = 'phone_no'
    REQUIRED_FIELDS = ['username','date_of_birth','first_name','last_name','gender']

    objects = MyAccountManager()

    def __str__(self):
        return "username:"+self.username +"  date_of_join:" + self.date_joined + "phone_number:" +self.phone_no + "Gender:" + self.gender
    
    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,opp_Label):
        return True




