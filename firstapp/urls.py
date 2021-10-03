from django.urls import path
from  . import views


urlpatterns = [
    # as_view is class method, and u can call using classname.method 
    path('',views.Index.as_view(), name="index"),
    # path('index',views.index,name="index")
    path('contactus/',views.contactus2, name = "contactus"),
    path('contactclass/',views.ContactUs.as_view(),name="contactclass"),
    
    # Aythnetication ENDPOINT
    # path('signup',views.RegistrationViewSeller.as_view())
    path('signup/',views.RegistrationView.as_view(), name="signup"),
    path('login/',views.LoginViewer.as_view(), name="login"),
    path('logout',views.LogoutUser.as_view(),name='logout'),
    path('signupseller/',views.RegisterViewSeller.as_view(),name='loginseller')
]   