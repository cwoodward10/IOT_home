from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import post

class IndexView(generic.ListView):
	template_name = 'home/index.html'
	context_object_name = 'latest_post_list'

	def get_queryset(self):

		return post.objects.filter(
			pub_date__lte = timezone.now()
		).order_by('-pub_date')[:5]
