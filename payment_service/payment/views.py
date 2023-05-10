from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

import json

from django.views.decorators.csrf import csrf_exempt
from payment.models import payment_status as paystat
from shipment_update.views import shipment_details_update as ship_update

def get_transaction_details(uname):
    user = paystat.objects.filter(username = uname)
    for data in user.values():
        return data

def store_data(uname, prodid, price, quantity, mode_of_payment, mobile):
    user_data = paystat(
        username = uname,
        product_id = prodid,
        price = price,
        quantity = quantity,
        mode_of_payment = mode_of_payment,
        mobile = mobile,
        status = "Success"
    )

    user_data.save()
    return 1

# Khi gửi một request HTTP, trình duyệt nhận về Cookie
@csrf_exempt
def init_payment(request):
    uname = request.POST.get("User Name")
    prodid = request.POST.get("Product id")
    price = request.POST.get("Product price")
    quantity = request.POST.get("Product quantity")
    mode_of_payment = request.POST.get("Payment mode")
    mobile = request.POST.get("Mobile Number")

    resp = {}
    print(uname,prodid,price,quantity,mode_of_payment,mobile)
    if uname and prodid and price and quantity and mode_of_payment and mobile:
        
        respdata = store_data(
            uname,
            prodid,
            price,
            quantity,
            mode_of_payment,
            mobile
        )
        print(respdata)
        # respdata2 = ship_update(uname)
        if respdata:
            print(uname,prodid,price,quantity,mode_of_payment,mobile)
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Transaction is completed.'
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Transaction is failed, Please try again.'
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'All fields are mandatory.'

    return HttpResponse(json.dumps(resp), content_type = 'application/json')


@csrf_exempt
def user_transaction_info(request):
    resp = {}
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            val1 = json.loads(request.body)
            uname = val1.get('User Name')
            
            if uname:
                respdata = get_transaction_details(uname)

                if respdata:
                    resp['status'] = 'Success'
                    resp['status_code'] = '200'
                    resp['data'] = respdata
                else:
                    resp['status'] = 'Failed'
                    resp['status_code'] = '400'
                    resp['message'] = 'User Not Found.'
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Fields is mandatory.'
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Request type is not matched.'

    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Request type is not matched.'

    return HttpResponse(json.dumps(resp), content_type = 'application/json')