from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
   template_name='home.html'
   

class AboutBookView(TemplateView):
   template_name='about.html'

class SayBookView(TemplateView):
   template_name='say.html'
   
class Form(TemplateView):
   template_name='form.html'
   
class Img(TemplateView):
   template_name='img.html'
   
class Wellcome(TemplateView):
   template_name='wellcome.html'