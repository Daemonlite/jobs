from audioop import reverse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from flask import message_flashed

from .models import *
# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('jobs')

class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('jobs')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('jobs')
        return super(RegisterPage, self).get(*args, **kwargs)

def jobs(request):
 
 obj = Company.objects.all()
 context={
        "obj":obj,
    }
 return render(request,'base/jobs.html',context)

class Application(LoginRequiredMixin, CreateView):
    model = Application
    fields = ['Full_name','Age','Residence','number','email','Cv']
    template_name = 'base/application.html'
    success_url = reverse_lazy('jobs')

    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Application, self).form_valid(form)

def individual(request):
    ind = Individual.objects.all()
    context={
        "ind":ind,
    }
    return render(request,'base/individual.html',context)

       

class Individual_form(LoginRequiredMixin,CreateView):
    model = Individual
    fields = ['Full_name','job_title','job_descr','amount_due','address']
    template_name = 'base/individual_form.html'
    success_url = reverse_lazy('individual')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Individual_form, self).form_valid(form)

class add_company(LoginRequiredMixin,CreateView):
   model = Company
   fields = ['Name','about','is_hiring','profile']
   template_name = 'base/company.html'
   success_url = reverse_lazy('jobs')

   def form_valid(self, form):
        form.instance.user = self.request.user
        return super(add_company, self).form_valid(form)




