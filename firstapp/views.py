from re import TEMPLATE
from django.shortcuts import redirect, render,HttpResponse
from django.views.generic import TemplateView
from django.core.exceptions import ValidationError
from django.views.generic.edit import CreateView
from .forms import ContactUsForm,RegistrationForm, RegistrationFormSeller, RegistrationFormSeller2
from django.views.generic import FormView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import SellerAdditional,CustomUser


# Create your views here.

# Function based views 
# def index(request):
#     age = ['vikram','raj','pinki','dink']
#     dic = {"a":"one","b":"two","c":"three"}
#     return render(request,'firstapp/index.html',{"age":age,"dic":dic})

# class based view
class Index(TemplateView):
    template_name = "firstapp/index.html"

    def get_context_data(self, **kwargs):
        age = 100

        age = ['vikram','raj','pinki','dink']
        dic = {"a":"one","b":"two","c":"three"}

        context_old = super().get_context_data(**kwargs)
        context = {'age':age, "dic":dic,"context_old":context_old}

        return context


# def contactus(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         if len(phone)<10 or len(phone)>10:
#             return HttpResponse("Wrong Phone")
#             raise ValidationError("Phone number should be of length 10")
#         query = request.POST.get('query')
#         print(name + " " + email + " " + phone + " " + query)
#     return render(request,'firstapp/contactus.html')


def contactus2(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():      #clean_data
            if len(form.cleaned_data.get('query'))>10:
                form.add_error('query', 'Query length is not right')
                return render(request, 'firstapp/contactus2.html', {'form':form})
            form.save()
            return HttpResponse("Thank YOu")
        else:
            if len(form.cleaned_data.get('query'))>10:
                #form.add_error('query', 'Query length is not right')
                form.errors['__all__'] = 'Query length is not right. It should be in 10 digits.'
            return render(request, 'firstapp/contactus2.html', {'form':form})
    return render(request, 'firstapp/contactus2.html', {'form':ContactUsForm})


class ContactUs(FormView):
    form_class = ContactUsForm
    template_name = 'firstapp/contactus2.html'

    success_url = '/'

    def form_valid(self,form):
        if len(form.cleaned_data.get('query'))>10:
            form.add_error('query','Query length is not right')
            return render(self.request,'firstapp/constactus2.html',{'form':form})
        form.save()
        response = super().form_valid(form)
        return response

    def form_invalid(self,form):
        if len(form.cleaned_data.get('query'))>10:
            form.add_error('query','Query Length not right')
        response = super().form_invalid(form)

# class RegistrationViewSeller(CreateView):
#     form_class = RegistrationFormSeller
#     template_name = 'firstapp/register.html'
#     success_url = "/"

#     def post(self,request,*args,**kwargs):
#         response = super().post(request,*args,**kwargs)

#         # if user is created then we add seller additional for that seller
#         if response.status_code == 302:
#             gst = request.POST.get('gst')
#             warehouse_location = request.POST.get('warehouse_location')
#             # get the email from response and get the custom user for that email which exist
#             email = request.POST.get('email')
#             user = CustomUser.objects.get(email=email)

#             # create Seller additional object for the user
#             s_add = SellerAdditional.objects.create(user=user,gst=gst,warehouse_location=warehouse_location)
#             return response
#         else:
#             return response



from django.core.mail import EmailMessage,send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes,force_text
# Encode a bytestring to a base64 string for use in URLs. Strip any trailingequal signs.
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
#Load a template and render it with a context. Return a string.template_name may be a string or a list of strings.
from django.template.loader import render_to_string
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'firstapp/registerBasicUser.html'
    success_url = '/login'

    # adding email verification

    def post(self,request,*args,**kwargs):
        # form = RegistrationForm(request.POST)
        # calling super saves the user
        response = super().post(request,*args,**kwargs)
        user_email = request.POST.get('email')
        # 302 means success
        if response.status_code ==302:
            user = CustomUser.objects.get(email=user_email)
            # making user active false untill verified
            user.is_active = False
            user.save()

            current_site = get_current_site(request) #www.wondershop.com
            mail_subject = 'Activate your account'
            message = render_to_string('firstapp/registration/acc_active_email.html',{
                'user':user,
                'domain' : current_site.domain,
                'uid' : urlsafe_base64_encode(force_bytes(user.pk))

            })


class LoginViewer(LoginView):
    template_name = 'firstapp/login.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        self.redirect_authenticated_user = True
        return super().dispatch(request,*args, **kwargs)
    
class LogoutUser(LogoutView):
    success_url = '/'




# THis form only accessible if user is logged in
# class RegisterViewSeller(LoginRequiredMixin,CreateView):
#     template_name = 'firstapp/registerseller.html'
#     form_class = RegistrationFormSeller2
#     success_url = reverse_lazy("index")

#     def form_valid(self,form):
#         # request has user object as logged in
#         user = self.request.user
#         user.type.append(user.Types.Seller)
#         user.save()
#         form.instance.user = self.request.user
#         return super().form_valid(form)

def testsession(request):
    if request.session.get('test',False):
        print(request.session('test'))
    
    request.session.set_expiry(1)

    try:
        request.session['test'] = request.user.name
    except:
        request.session['test'] = "Not logged in"
    return render(request,'firstapp/testsession.html')