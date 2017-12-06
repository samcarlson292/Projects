from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import ArtistsProper, SongsProper
from django.views import generic

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import StringIO, PIL.Image

def search(request):
	search_term = None
	search_type = "artist"

	if request.GET:
		search_term = request.GET['search_term']
		search_type = request.GET['search_type']
	if (search_type == "artist"):
		search_results = ArtistsProper.objects.filter(artist_name=search_term).order_by('collection_time')
	else:
		spotify_results = SongsProper.objects.filter(song_name=search_term).order_by('artist_id','collection_time')

	if (search_type == 'artist'):
		time = [result.collection_time for result in search_results]
		popularity = [result.artist_popularity for result in search_results]
		fig = plt.figure()
		ax = fig.add_subplot(111)
		ax.plot(time, popularity)

		ax.set_xlabel('Time')
		ax.set_ylabel('Popularity')
		ax.set_title('Popularity Trend for ' + str(search_term))

		image_str = StringIO.StringIO()
		fig.savefig(image_str, format='PNG')
		image_str.seek(0)
		image = Image.fromstring('RGB', (1200, 800), image_str)
		image.save(image_str, 'PNG')
	else:
		time = [result.collection_time for result in spotify_results]
		popularity = [result.song_popularity for result in spotify_results]
		fig = plt.figure()
		ax = fig.add_subplot(111)
		ax.plot(time, popularity)

		ax.set_xlabel('Time')
		ax.set_ylabel('Popularity')
		ax.set_title('Popularity Trend for ' + str(search_term))

		image_str = stringIO.StringIO()
		fig.savefig(image_str, format='PNG')
		image_str.seek(0)
		image = Image.fromstring('RGB', (1200, 800), image_str)
		image.save(image_str, 'PNG')	

	return render(request,'tuneApp/search.html', {'object_list' : search_results, 'data_type' : search_type, 'chart': image_str.getvalue())
