from django.contrib import admin
from .models import *
from django.contrib.auth.admin import  UserAdmin


from django.contrib.auth.models import  User
from .forms import CustomUserCreationForm,CustomUserChangeForm
from .models import CustomUser
# Register your models here.


admin.site.register(CustomerAdditional)
admin.site.register(SellerAdditional)

class ProductInCartInline(admin.TabularInline):
    model = ProductInCart

class CartInline(admin.TabularInline):
    model = Cart

class DealInline(admin.TabularInline):
    model = Deal.user.through

class SellerAdditionalInline(admin.TabularInline):
    model = SellerAdditional

# CustomUser Admin
class  CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email','name','is_staff', 'is_active','type')
    list_filter = ('email', 'is_staff', 'is_active','type')
    fieldsets = (
        (None, {'fields': ('email','name','password','type',)}), #usertype 2
        ('Permissions', {'fields': ('is_staff', 'is_active',)}),#'is_customer','is_seller'
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','name','password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser,CustomUserAdmin)


# its for default user model only
# class UserAdmin(UserAdmin):
#     model = User
#     list_display = ('username', 'get_cart', 'is_staff', 'get_order',)
#     list_filter = ('username', 'is_staff', 'is_active', 'is_superuser')
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Permissions', {'fields': ('is_staff', ('is_active' , 'is_superuser'), )}),
#         ('Important dates',{'fields': ('last_login', 'date_joined')}),
#         # ('Cart', {'fields': ('get_cart',)})
#         ('Advanced options', {
#             'classes': ('collapse',),
#             'fields': ('groups', 'user_permissions'),
#         }),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),   # class for css 
#             'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser', 'groups')}     # fields shown on create user page on admin panel
#         ),
#     )
#     inlines = [
#         CartInline, DealInline
#     ]
#     def get_order(self,obj):
#         return obj.order.all().first()
#     def get_cart(self,obj):       # this function only works in list_display
#         return obj.cart           # through reverse related relationship
#     search_fields = ('username',)     #search_filter for search bar
#     ordering = ('username',)

# unregister defualt User and then register own user
# admin.site.unregister(User)
# admin.site.register(User,UserAdmin)


# Customize admin for Cart
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    model = Cart
        # here user__is_staff wont work 
    list_display = ('staff','user','created_on',) #here user__is_staff won't work
    list_filter = ('user','created_on',)
    fieldsets = (
        ('None',{'fields': ('user','created_on',)}), #only direct relationshio no nested relationship( '__' ) like user__is_staff
        # ('User',{'fields':('staff')})
    )
    inlines = (
        ProductInCartInline,
    )

    #to display only in list_display
    def staff(self,obj):
        return obj.user.is_staff

    staff.admin_order_field = 'user__is_staff' #allows column order sorting
    staff.short_description = 'Staff User' #rename col head

    #filter on side bar for some reason this works
    list_filter = ['user__is_staff','created_on'] #with direct forign key()user no error but not shown in filters, with function error
    ordering = ['user__username']
    search_fields = ['user__username'] #with foreign key no error but filtering not possible directly

# @admin.register(Cart) # through register decorator
# class CartAdmin(admin.ModelAdmin):
#     model = Cart
#     list_display = ('user','staff', 'created_on',)    # here user__is_staff will not work   
#     list_filter = ('user', 'created_on',)
#     #fields = ('staff',)           # either fields or fieldset
#     fieldsets = (
#         (None, {'fields': ('user', 'created_on',)}),   # only direct relationship no nested relationship('__') ex. user__is_staff
#         #('User', {'fields': ('staff',)}),
#     )
#     inlines = (
#         ProductInCartInline,
#     )
#     # To display only in list_display
#     def staff(self,obj):
#         return obj.user.is_staff
#     # staff.empty_value_display = '???'
#     staff.admin_order_field  = 'user__is_staff'  #Allows column order sorting
#     staff.short_description = 'Staff User'  #Renames column head

#     #Filtering on side - for some reason, this works
#     list_filter = ['user__is_staff', 'created_on',]    # with direct foreign key(user) no error but not shown in filters, with function error
#     # ordering = ['user',]
#     search_fields = ['user__username']     # with direct foreign key no error but filtering not possible directly


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    inlines = [
        DealInline,
    ]
    # exclude = ('user',)

class SellerAdmin(admin.ModelAdmin):
    inlines = [
        SellerAdditionalInline
    ]





admin.site.register(Contact)

admin.site.register(Product)
admin.site.register(ProductInCart)
admin.site.register(Order)
# admin.site.register(UserType)
admin.site.register(Customer)
admin.site.register(Seller,SellerAdmin)