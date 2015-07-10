from django.http import HttpResponse
from django.utils import simplejson

from google.appengine.api import urlfetch


import urllib
import string 

def vat(request, country_code, vat_no):

	country_code = string.upper(country_code)
	
	data=dict(ms=country_code, iso=country_code, vat=vat_no)
	payload = urllib.urlencode(data)
	result = urlfetch.fetch(url='http://ec.europa.eu/taxation_customs/vies/viesquer.do', payload=payload, method=urlfetch.POST, headers={'Content-Type': 'application/x-www-form-urlencoded'})
	
	content = result.content

	json = 'true' if 'Yes, valid VAT number' in content else 'false'
	
	if 'Member State service unavailable.' in content:
		# Error, the member state service is not available
		json = simplejson.dumps(dict(error=True, error_code=1, error_message='Member State service unavailable.'))

	if 'callback' in request.GET:
		json = request['callback'] + '(' + json + ')'
		
	response = HttpResponse(json, mimetype='application/javascript')

	return response