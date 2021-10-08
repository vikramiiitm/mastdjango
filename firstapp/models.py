from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import AutoField
from django.utils import timezone
from multiselectfield import MultiSelectField# Create your models here.
from django.db.models import Q

from django.core.validators import RegexValidator

from django.contrib.auth.models import  AbstractUser,AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager
from django.contrib.auth.models import PermissionsMixin

"""
# 3 Separate class for different rolles and many to many field in user model
class UserType(models.Model):
    CUSTOMER = 1S
    SELLER = 2
    TYPE_CHOICES = (
        (SELLER, 'Seller'),
        (CUSTOMER, 'Customer')
    )

    id = models.PositiveSmallIntegerField(choices=TYPE_CHOICES,primary_key=True)
    def __str__(self):
        return self.get_id_display()
"""

# # Custom User
# class CustomUser(AbstractUser):
#     # making default username to none instead using email as username field
#     username = None
#     email = models.EmailField(_('email address'),unique=True)
#     name = models.CharField(max_length=255)

#     """
#     Multiple user type without extra fields
#     # 1. Boolean Select Field
#     # option to make if user is seller or customer
#     is_customer = models.BooleanField(default=True)
#     is_seller = models.BooleanField(default=False)

#     # 2 Choice Field with djnago multiselect
#     # type = (
#         # (1, 'Seller'), 
#         # (2, 'Customer')
#     # )
#     # to select one of two choice, to select multi instal package django-multiselectfield
#     # user_type = models.IntegerField(choices=type, default=1)

#     # 3 Separate class for different rolles and many to many field in user model
#     # usertype = models.ManyToManyField(UserType)

#     """
#     # Multiple user with extra field
#     # 1 boolean field with class for different role
#     # is_customer = models.BooleanField(default=True)
#     # is_seller = models.BooleanField(default=False)


#     # Proxy model
#     class Types(models.TextChoices):
#         CUSTOMER = "Customer", "CUSTOMER"
#         SELLER = "Seller","SELLER"
    
#     default_type = Types.CUSTOMER
#     type = models.CharField(_('Type'),max_length=255, choices=Types.choices, default=default_type)

#     # if not code below then taking default value in user model not in proxy in model
#     # The point is that we do not know what arguments save is expecting so this is 
#     # basically saying "any arguments passed into our new save(...) method,
#     # just hand them off to the old overridden save(...) method,
#     # positional arguments first followed by any keyword arguments"
#     def save(self, *args, **kwargs):
#         if not self.id:
#             self.type = self.default_type
#         return super().save(*args, **kwargs)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']

#     # specify all objects for the class comes from
#     objects = CustomUserManager()

#     def __str__(self):
#         return self.name

class LowercaseEmailField(models.EmailField):
    """
    Override EmailField to convert emails to lowercase before saving.
    """
    def to_python(self, value):
        """
        Convert email to lowercase.
        """
        value = super(LowercaseEmailField, self).to_python(value)
        # Value can be None so check that it's a string before lowercasing.
        if isinstance(value, str):
            return value.lower()
        return value

class CustomUser(AbstractBaseUser,PermissionsMixin):
    # username = None
    email = LowercaseEmailField(_('email address'), unique=True)
    name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    # if you require phone number field in your project
    phone_regex = RegexValidator( regex = r'^\d{10}$',message = "phone number should exactly be in 10 digits")
    phone = models.CharField(max_length=255, validators=[phone_regex], blank = True, null=True)  # you can set it unique = True

    # is_customer = models.BooleanField(default=True)
    # is_seller = models.BooleanField(default = False)

    # type = (
    #     (1, 'Seller'),
    #     (2, 'Customer')
    # )
    # user_type = models.IntegerField(choices = type, default=1)

    #usertype = models.ManyToManyField(UserType)

    class Types(models.TextChoices):
        SELLER = "Seller", "SELLER"
        CUSTOMER = "Customer", "CUSTOMER"
    
    # Types = (
    #     (1, 'SELLER'),
    #     (2, 'CUSTOMER')
    # )
    # type = models.IntegerField(choices=Types, default=2)

    default_type = Types.CUSTOMER

    #type = models.CharField(_('Type'), max_length=255, choices=Types.choices, default=default_type)
    type = MultiSelectField(choices=Types.choices, default=[], null=True, blank=True)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    #place here
        # if not the code below then taking default value in User model not in proxy models
    def save(self, *args, **kwargs):
        if not self.id:
            #self.type = self.default_type
            self.type.append(self.default_type)
        return super().save(*args, **kwargs)


"""
Multiple usertype with extra fields
1.Boolean field + separate class for different users
type with one to one field


class Customer(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address = models.CharField(max_length=1000)

    def __str__(self):
        return self.user.email

class Seller(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    gst = models.CharField(max_length=10)
    warehouse_location = models.CharField(max_length=1000)

    def __str__(self):
        return self.user.email
"""
# proxy model Manager
class SellerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        #return super().get_queryset(*args, **kwargs).filter(type = CustomUser.Types.SELLER)
        return super().get_queryset(*args, **kwargs).filter(Q(type__contains = CustomUser.Types.SELLER))

class CustomerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        #return super().get_queryset(*args, **kwargs).filter(type = CustomUser.Types.CUSTOMER)
        return super().get_queryset(*args, **kwargs).filter(Q(type__contains = CustomUser.Types.CUSTOMER))
        

# proxy model by subclassing CustomUser setting meta property proxy true
# class Seller(CustomUser):
#     default_type = CustomUser.Types.SELLER
#     objects = SellerManager()
#     class Meta:
#         proxy = True

#     def  sell(self):
#         print("I can sell")

# class Customer(CustomUser):
#     default_type = CustomUser.Types.CUSTOMER
#     objects = CustomerManager()
#     class Meta:
#         proxy = True
    
#     def buy(self):
#         print("I can Buy")


# proxy
class CustomerAdditional(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address = models.CharField(max_length=1000)

    def __str__(self):
        return self.user.email

class SellerAdditional(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    gst = models.CharField(max_length=10)
    warehouse_location = models.CharField(max_length=1000)

    def __str__(self):
        return self.user.email

# Proxy Models. They do not create a seperate table
class Seller(CustomUser):
    default_type = CustomUser.Types.SELLER
    objects = SellerManager()
    class Meta:
        proxy = True
    
    def sell(self):
        print("I can sell")

    @property
    def showAdditional(self):
        return self.selleradditional

class Customer(CustomUser):
    default_type = CustomUser.Types.CUSTOMER
    objects = CustomerManager()
    class Meta:
        proxy = True 

    @property
    def showAdditional(self):
        return self.customeradditional

    def buy(self):
        print("I can buy")


 


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="firstapp/productimages",default=None,null=True,blank=True)
    price = models.FloatField()

    @classmethod
    def updateprice(cls,product_id,price):
        product = cls.objects.filter(product_id = product_id)
        product = product.first()
        product.price = price
        product.save()
        return product

    @classmethod
    def create(cls,product_name, price):
        product = Product(product_name = product_name, price = price)
        product.save()
        return product

    def __str__(self):
        return self.product_name

# Cart Model Manager
class CartManager(models.Manager):
    # method to create cart for user
    def create_cart(self, user):
        cart = self.create(user = user)
        return cart

class  Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='cart')
    created_on = models.DateTimeField(default = timezone.now)

    # instantiating Cart manager
    objects = CartManager()

class ProductInCart(models.Model):
    class Meta:
        unique_together = (('cart','product'),)
    product_in_cart_id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Order(models.Model):
    status_choices = {
        (1, 'Not Packed'),
        (2, 'Ready For Shipment'),
        (3, 'Shipped'),
        (4, 'Delivered')
    }
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='order')
    status = models.IntegerField(choices = status_choices, default=1)

class Deal(models.Model):
    user = models.ManyToManyField(CustomUser)
    deal_name = models.CharField(max_length=255, blank=True)


# modelform
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_regex = RegexValidator(regex = r'^\+?1?\d{10}$',message="The format 99999999 upto 14 digit")  
    phone = models.CharField(max_length=255,validators=[phone_regex])
    query = models.TextField()

    def __str__(self):
        return self.name + " " + self.query 