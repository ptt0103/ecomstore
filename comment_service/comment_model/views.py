from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json

from django.views.decorators.csrf import csrf_exempt
from comment_model.models import comment_Model

@csrf_exempt
def get_comments(request):
    data = []
    resp = {}

    comment_data = comment_Model.objects.all()

    for tbl_value in comment_data.values():
        data.append(tbl_value)

    if data:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = data
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Data is not available.'

    return HttpResponse(json.dumps(resp, indent = 4, sort_keys = True, default = str), content_type = 'application/json')

def data_insert(content, userId, userName, dateComment):
    comment_data = comment_Model(
        content = content,
        userId = userId,
        userName = userName,
        dateComment = dateComment
    )
    comment_data.save()
    return 1

@csrf_exempt
# get the data from the front end.
def insertComment_req(request):
    content = request.POST.get("Content")
    userId = request.POST.get("User id")
    userName = request.POST.get("User name")
    dateComment = request.POST.get("Date comment")
    resp = {}

    # checking that all fields are available.
    if content and userId and userName and dateComment :
        respdata = data_insert(content, userId, userName, dateComment)

        # if it returns value then will show success.
        if respdata:
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Comment is insert Successfully.'
        # else returning any value then the show will fail.
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Unable insert comment, Please try again.'
    # if any field is missing.
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'All fields are mandatory.'

    return HttpResponse(json.dumps(resp), content_type = "application/json")

@csrf_exempt
def get_comments_beLongOf(request):
    UserId = request.POST.get("User id")
    data = []
    resp = {}
    comment_data = comment_Model.objects.filter(userId=UserId)

    for tbl_value in comment_data.values():
        data.append(tbl_value)

    if data:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = data
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Data is not available.'

    return HttpResponse(json.dumps(resp, indent = 4, sort_keys = True, default = str), content_type = 'application/json')