from django.shortcuts import render
import requests
from django.shortcuts import *
from django.template import RequestContext
from django.contrib.auth import *
from django.contrib.auth.models import Group, User

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import Max,Count
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from django.db import transaction
from django.contrib.auth.hashers import *
from django.core.mail import send_mail

from django.utils.six.moves import range
from django.http import StreamingHttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_exempt
import time
import collections
import xlrd
import json 
import csv
import simplejson
import xlwt
import requests
import os
from django.contrib.auth import authenticate, login


from datetime import datetime,timedelta
from django.contrib.auth import authenticate

from django.contrib.sites.shortcuts import get_current_site
from django.core import serializers



from django.http import HttpResponse, JsonResponse

# Create your views here.

@csrf_exempt
def login(request):


	r=requests.get('https://www.ccf.com.pe/webresources/login/jara/12345')
	data= r.text

	return HttpResponse(data, content_type="application/json")




@csrf_exempt
def reporte1(request):


	r=requests.get('https://www.ccf.com.pe/webresources/reporte1/3/2')
	data= r.text

	return HttpResponse(data, content_type="application/json")



@csrf_exempt
def reporte2(request):


	r=requests.get('https://www.ccf.com.pe/webresources/reporte2/1/2')
	data= r.text

	return HttpResponse(data, content_type="application/json")


@csrf_exempt
def reporte3(request):


	r=requests.get('https://www.ccf.com.pe/webresources/reporte3/4/2')
	data= r.text

	return HttpResponse(data, content_type="application/json")

@csrf_exempt
def reporte4(request):


	r=requests.get('https://www.ccf.com.pe/webresources/reporte4/5/3')
	data= r.text

	return HttpResponse(data, content_type="application/json")	

	