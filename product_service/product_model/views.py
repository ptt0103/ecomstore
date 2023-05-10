from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import requests
import json
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from product_model.models import product_details
from django.core import serializers
@csrf_exempt
def get_product_data(request):
    data = []
    resp = {}

    prod_data = product_details.objects.all()

    for tbl_value in prod_data.values():
        data.append(tbl_value)

    if data:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = data
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Data is not available.'

    return HttpResponse(json.dumps(resp), content_type = 'application/json')



def get_books_data(request):
    r = requests.get('http://127.0.0.1:8000/get_books/',headers = {'Content-Type': 'application/json'})
    data = r.json()
    return HttpResponse(json.dumps(data['data']), content_type = 'application/json')
        
def get_clothes_data(request):
    r = requests.get('http://127.0.0.1:5001/get_clothes/',headers = {'Content-Type': 'application/json'})
    data = r.json()
    return HttpResponse(json.dumps(data['data']), content_type = 'application/json')
        
def get_shoes_data(request):
    r = requests.get('http://127.0.0.1:4001/get_shoes/',headers = {'Content-Type': 'application/json'})
    data = r.json()
    return HttpResponse(json.dumps(data['data']), content_type = 'application/json')
        