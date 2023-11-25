from django.contrib.gis.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


# Create your models here.
class Province(models.Model):
    province_name = models.CharField(max_length=255)
    code_province = models.CharField(max_length=20, null=True)
    create_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'provinces'

    def __str__(self):
        return self.province_name


class Department(models.Model):
    department_name = models.CharField(max_length=255)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    create_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'departments'

    def __str__(self):
        return self.department_name


class Municipality(models.Model):
    municipality_name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    create_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'municipalities'

    def __str__(self):
        return self.municipality_name


class Shop(models.Model):
    shop_name = models.CharField(max_length=255)
    shop_description = models.CharField(max_length=255, null=True)
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE)
    shop_logo = models.FileField(upload_to='shop')
    shop_backdrop = models.FileField(upload_to='shop')
    shop_address = models.CharField(max_length=255, null=True)
    shop_latitude = models.FloatField(null=True)
    shop_longitude = models.FloatField(null=True)

    class Meta:
        managed = True
        db_table = 'shops'

    def __str__(self):
        return self.shop_name


class Shelve(models.Model):
    shelve_name = models.CharField(max_length=255)
    shelve_description = models.CharField(max_length=255, null=True)

    # shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'shelves'

    def __str__(self):
        return self.shelve_name


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_description = models.CharField(max_length=255, null=True)
    product_price = models.FloatField(default=0.0)
    product_in_promotion = models.BooleanField(default=False)
    product_promotion_price = models.FloatField(default=0.0)
    product_image = models.FileField(upload_to='products', null=True)

    # shelve = models.ForeignKey(Shelve, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'products'

    def __str__(self):
        return self.product_name


class ShopShelve(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    shelve = models.ForeignKey(Shelve, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'shop_shelves'

    def __str__(self):
        return self.shop.shop_name + ' | ' + self.shelve.shelve_name


class ShelveProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shop_shelve = models.ForeignKey(ShopShelve, on_delete=models.CASCADE)
    product_price = models.FloatField(default=0.0)

    class Meta:
        managed = True
        db_table = 'products_shelves'


class UserRole(models.Model):
    role_value = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'roles'

    def __str__(self):
        return self.role_value


class AppUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('An email is required.')
        if not password:
            raise ValueError('A password is required.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, municipality, role, password=None, **extra_fields):
        if not email:
            raise ValueError('An email is required.')
        if not password:
            raise ValueError('A password is required.')

        # Check if Municipality is provided and retrieve the Municipality instance if it is
        if municipality:
            try:
                municipality_instance = Municipality.objects.get(pk=municipality)
            except Municipality.DoesNotExist:
                raise ValueError('Invalid city ID')
            extra_fields['municipality'] = municipality_instance

        if role:
            try:
                role_instance = UserRole.objects.get(pk=role)
            except UserRole.DoesNotExist:
                raise ValueError('Invalid city ID')
            extra_fields['role'] = role_instance

        user = self.create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class AppUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'role']
    objects = AppUserManager()

    class Meta:
        managed = True
        db_table = 'users'

    def __str__(self):
        return self.username


class Client(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    quarter = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'clients'
