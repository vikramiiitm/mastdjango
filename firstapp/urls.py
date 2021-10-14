from django.urls import path
from  . import views
from django.urls import  reverse_lazy
from django.contrib.auth import views as auth_views
from  django.contrib import admin

from django.urls import reverse_lazy
urlpatterns = [
    # as_view is class method, and u can call using classname.method 
    path('admin/',admin.site.urls),
    path('',views.Index.as_view(), name="index"),
    # path('index',views.index,name="index")
    path('contactus/',views.contactus2, name = "contactus"),
    path('contactclass/',views.ContactUs.as_view(),name="contactclass"),
    
    # Aythnetication ENDPOINT
    # path('signup',views.RegistrationViewSeller.as_view())
    path('signup/',views.RegisterView.as_view(), name="signup"),
    path('login/',views.LoginViewer.as_view(), name="login"),
    path('logout',views.LogoutUser.as_view(),name='logout'),
    # path('signupseller/',views.RegisterViewSeller.as_view(),name='signupseller')
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    # session
    path('test',views.testsession, name="testsession"),

    # password change
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='firstapp/registration/password_change.html', success_url = reverse_lazy("password_change_done")), name='password_change'),
    path('password_change_done',auth_views.PasswordChangeDoneView.as_view(template_name="firstapp/registration/password_change_done.html"),name="password_change_done"),

    # Forgot password using email
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name = "firstapp/registration/password_reset.html"
    ,success_url = reverse_lazy("password_reset_done"),email_template_name = 'firstapp/registration/forgot_password_email.html'),name="reset_password"),

    path('reset_reset_sent/',auth_views.PasswordResetDoneView.as_view(template_name = "firstapp/registration/password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = "firstapp/registration/password_reset_form.html",success_url = reverse_lazy("password_reset_complete")),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name = "firstapp/registration/password_reset_done.html"),name="password_reset_complete"),

    #productlist
    path('listproduct',views.ListProducts.as_view(),name="listproduct"), 
    path('productdetail/<int:pk>',views.ProductDetail.as_view(),name='productdetail'),
    path('addtocart/<int:id>',views.addToCart,name='addtocart'),
    path('displaycart/',views.DisplayCart.as_view(),name="displaycart"),
    path('updatecart/',views.UpdateCart.as_view(),name="updatecart")
]


# when debugging true
from  django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)