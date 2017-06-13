from django.shortcuts import render
from django.views.generic.list import ListView
from posts.models import Record

class RecordListView(ListView):
	model = Record