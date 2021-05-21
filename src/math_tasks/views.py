from django.shortcuts import render

from .models import Task

import requests
from bs4 import BeautifulSoup as bs
# Create your views here.

def task_detail_view(request):

	r = requests.get('https://zadania.info/d16/1040241')
	print("page status code: ", r.status_code)
	
	soup = bs(r.text, 'html.parser')
	content = soup.find_all('p')[1].get_text()

	# r = requests.get('https://www.kwestiasmaku.com/przepis/ciasteczka-z-nutella')
	# soup = bs(r.text, 'lxml')
	# content = soup.select_one('div[class^="field field-name-field-przygotowanie field-type-text-long field-label-above"]').text

	obj = Task.objects.create(content=content)
	
	context = {
		'obj': obj
	}
	return render(request, "task_detail.html", context)