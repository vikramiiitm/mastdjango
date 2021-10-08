from django.urls import path
from  . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
urlpatterns = [
    # as_view is class method, and u can call using classname.method 
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
    path('password_change',auth_views.PasswordChangeView.as_view(template_name="firstapp/registration/password_change.html"),name="password_change"),
    path('password_change_done',auth_views.PasswordChangeView.as_view(template_name="firstapp/registration/password_change_done.html"),name="password_change_done")

]   