from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView, ListView,DetailView,CreateView,UpdateView,DeleteView
from myapp import models
from django.urls import reverse_lazy

class IndexView(ListView):
    context_object_name = 'musician_list'
    model = models.Musician
    template_name = 'myapp/index.html'

class MusicianDetails(DetailView):
    context_object_name = 'musician'
    model = models.Musician
    template_name = 'myapp/musicain_details.html'

class AddMusician(CreateView):
    fields = ('first_name', 'last_name', 'instrument')
    model = models.Musician
    template_name = 'myapp/musician_form.html'

class UpdateMusician(UpdateView):
    fields = ('first_name','last_name' ,'instrument')
    model = models.Musician
    template_name = 'myapp/musician_form.html'

class DeleteMusician(DeleteView):
    context_object_name = 'musician'
    model = models.Musician
    success_url = reverse_lazy('myapp:index')
    template_name = 'myapp/delete_musician.html'
