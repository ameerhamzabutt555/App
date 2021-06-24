from django.http import HttpResponse
from .models import students
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import RedirectView, TemplateView
from .forms import feedback
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django import forms

class student(DetailView):  #show all data students but one by one
    model = students

class show_students(ListView):    #show all data students
    model = students

class student_form(CreateView):   #message form
    template_name = 'app/student_form.html'
    model = students
    fields = ['name','course','age']
    success_url = '/app/students/'

    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget=forms.TextInput(attrs={'class':'name'})
        form.fields['course'].widget=forms.TextInput(attrs={'class':'course'})
        form.fields['age'].widget=forms.TextInput(attrs={'class':'age'})
        return form

class student_update(UpdateView):   #message form
    template_name = 'app/student_update.html'
    model = students
    fields = ['name','course','age']
    success_url = '/app/students/'

    def get_form(self):
        form = super().get_form() #this method give access perent class
        form.fields['name'].widget=forms.TextInput(attrs={'class':'name'})
        form.fields['course'].widget=forms.TextInput(attrs={'class':'course'})
        form.fields['age'].widget=forms.TextInput(attrs={'class':'age'})
        return form


class message_page(FormView):   #message form
    template_name = 'app/feedback.html'
    form_class = feedback
    success_url = '/app/thanks/'

class thanks_page(TemplateView):
    template_name = 'app/thanks.html'

class delet_page(DeleteView):   #message form
    template_name = 'app/delet.html'
    model = students
    success_url = '/app/students/'