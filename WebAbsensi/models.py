from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, nisn, username, name , password=None):
        if not nisn:
            raise ValueError('Users must have an NISN')
        if not username:
            raise ValueError('Users must have an username')
            
        user  = self.model(
                nisn=nisn,
                name=name,
                username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nisn, username, name, password):
        user  = self.create_user(
                nisn=nisn,
                name=name,
                username=username,
                password= password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class MasterSiswa(AbstractBaseUser):
    nisn                    = models.CharField(primary_key=True, unique=True,  max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])                                 
    name                    = models.CharField(max_length=100)
    username                = models.CharField(max_length=16, unique=True)
    date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin				= models.BooleanField(default=False)
    is_active				= models.BooleanField(default=True)
    is_staff				= models.BooleanField(default=False)
    is_superuser			= models.BooleanField(default=False)

    USERNAME_FIELD = 'nisn'
    REQUIRED_FIELDS = ['username', 'name']

    objects = MyAccountManager()

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class MasterKelas(models.Model):
    siswa                   = models.ForeignKey(MasterSiswa, on_delete=models.CASCADE)
    ID_KELAS                = (
                                ('01', '10'),
                                ('02', '11'),
                                ('03', '12'),
                                ('04', '13'),
                            )
    id_kelas                = models.CharField(max_length=100, choices=ID_KELAS)
    
class MasterJurusan(models.Model):
    siswa                   = models.ForeignKey(MasterSiswa, on_delete=models.CASCADE)
    ID_JURUSAN              = (
                                ('01', 'KGSP'),
                                ('02', 'SIJA'),
                                ('03', 'TEDK'),
                                ('04', 'TFLM'),
                                ('05', 'TMPO'),
                                ('06', 'TTL'),
                            )
    id_jurusan              = models.CharField(max_length=100, choices=ID_JURUSAN)

class Absensi(models.Model):
    siswa                   = models.ForeignKey(MasterSiswa, on_delete=models.CASCADE)
    checkin                 = models.DateTimeField(auto_now_add=True)
    checkout                = models.DateTimeField(auto_now=True)

