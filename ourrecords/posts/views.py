from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from posts.models import Record
from django.urls import reverse_lazy

class RecordListView(ListView):
	model = Record

class RecordDetailView(DetailView):
	model = Record

class RecordCreateView(CreateView):
	model = Record
	fields = ['title', 'slug', 'image', 'content']

class RecordUpdateView(UpdateView):
	model = Record
	fields = ['title', 'slug', 'image', 'content']
	template_name_suffix = '_update_form'

class RecordDeleteView(DeleteView):
	model = Record
	success_url = reverse_lazy('records_list')


















