from django.shortcuts import render

import json
import urllib
import os
# import sqlite
import sqlite3

from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render

import datetime
from django.utils import timezone
from django.db import models
# import flickr_api

from .models import *

# Create your views here.

def topPhotos(request):

	api_key = "40128fd9fbc72810e808909f7f24bc83"
	api_secret = "eeefb11ba8ea31e8"
	per_page = "10"
	pages = "1"
	today_date = datetime.datetime.now().strftime("%Y-%m-%d")

	topten_url = "https://api.flickr.com/services/rest/" + \
	"?method=flickr.photos.search" + \
	"&api_key=" + api_key + \
	"&min_upload_date=" + today_date + \
	"&max_upload_date=" + today_date + \
	"&sort=interestingness_desc" + \
	"&per_page=" + per_page + \
	"&page=" + pages + \
	"&format=json&nojsoncallback=1"

	response = urllib.request.urlopen(topten_url)
	str_response = response.readall().decode('utf-8')
	
	obj = json.loads(str_response)
	json_data = json.dumps(obj)

	photos = obj['photos']['photo']
	url_list = []

	for photo in photos:
		photo_id = str(photo['id'])
		secret = str(photo['secret'])
		server = str(photo['server'])
		farm   = str(photo["farm"])
		photo_url = "http://farm" + farm + ".staticflickr.com/" + server + "/" + photo_id + "_" + secret + "_b.jpg"
		url_list.append(photo_url)

	# Save to sqlite3 database.
	# cursor.execute('insert into File (id, url_list_store, url_list) values (?,?,?)', (id, name, sqlite3.Binary(file.read())))
	
	# conn = sqlite3.connect('/path/to/your/sqlite_file.db')
	# c = conn.cursor()
	# for item in my_list:
	# c.execute('insert into tablename values (?,?,?)', item)

	context = {'url_list': url_list}
	return render(request, 'topten/index.html', context)