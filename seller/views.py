from re import TEMPLATE
from django.shortcuts import redirect, render,HttpResponse
from django.views.generic import TemplateView
from django.core.exceptions import ValidationError
from django.views.generic.edit import CreateView
from firstapp.forms import ContactUsForm,RegistrationForm, RegistrationFormSeller, RegistrationFormSeller2
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from firstapp.models import SellerAdditional,CustomUser
# Create your views here.


def index(request):
    return render(request,'seller/index.html')

class LoginViewer(LoginView):
    template_name = 'seller/login.html'
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        self.redirect_authenticated_user = True
        return super().dispatch(request,*args, **kwargs)
    
class LogoutUser(LogoutView):
    success_url = reverse_lazy('index')

# THis form only accessible if user is logged in
class RegisterViewSeller(LoginRequiredMixin,CreateView):
    template_name = 'seller/registerseller.html'
    form_class = RegistrationFormSeller2
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        # request has user object as logged in
        user = self.request.user
        user.type.append(user.Types.SELLER)
        user.save()
        form.instance.user = self.request.user
        return super().form_valid(form)
