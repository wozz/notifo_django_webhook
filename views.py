import hashlib
from django.http import HttpResponse
import urllib
import notifo

API_KEY = '<API KEY>'
USER_NAME = '<USER NAME>'

def sig(vals):
	base = hashlib.sha1()
	for k in sorted(vals.items()):
		if vals['notifo_signature'] != vals[k[0]]:
			base.update(urllib.quote(vals[k[0]], safe=''))
	base.update(API_KEY)
	return base.hexdigest();

def notifo_webhook(request):
	if request.method == 'POST':
		if str(sig(request.POST)) == str(request.POST['notifo_signature']):
			resp = notifo.send_notification(USER_NAME, API_KEY, to=str(request.POST['notifo_from_username']), msg='boop')
	else:
		pass

	return HttpResponse('done')

