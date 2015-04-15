from django.shortcuts import render

import json
import urllib

from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render

import datetime
from django.utils import timezone
from django.db import models
# import flickr_api

from .models import *

# Create your views here.

def getTopPhotos(request):

	api_key = "40128fd9fbc72810e808909f7f24bc83"
	api_secret = "eeefb11ba8ea31e8"
	per_page = "10"
	pages = "1"

	# topten_url = "https://api.flickr.com/services/rest/" + 
	# "?method=flickr.photos.search" +
	# "&api_key=" + api_key + 
	# "&min_upload_date=" + "2015-04-14" + 
	# "&max_upload_date=" + "2015-04-14" + 
	# "&sort=interestingness_desc" + 
	# "&per_page=" + per_page +
	# "&page=" + pages +
	# "&format=json&nojsoncallback=1"
	
	topten_url = "https://api.flickr.com/services/rest/" + "?method=flickr.photos.search" + "&api_key=" + api_key +  "&min_upload_date=" + "2015-04-14" + "&max_upload_date=" + "2015-04-14" + "&sort=interestingness_desc" + "&per_page=" + per_page + "&page=" + pages + "&format=json&nojsoncallback=1"
	response = urllib.request.urlopen(topten_url)
	str_response = response.readall().decode('utf-8')
	obj = json.loads(str_response)
	json_data = json.dumps(obj)

	return HttpResponse(json_data, content_type='application/json')