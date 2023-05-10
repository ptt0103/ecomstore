from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
import json

from django.views.decorators.csrf import csrf_exempt
from user_model.models import user_registration

# inserting the data into the database table.
def data_insert(fname, lname, email, mobile, password, address):
    user_data = user_registration(
        fname = fname,
        lname = lname,
        email = email,
        mobile = mobile,
        password = password,
        address = address
    )

    user_data.save()
    return 1

@csrf_exempt
# get the data from the front end.
def registration_req(request):
    fname = request.POST.get("First Name")
    lname = request.POST.get("Last Name")
    email = request.POST.get("Email id")
    mobile = request.POST.get("Mobile Number")
    password = request.POST.get("Password")
    cnf_password = request.POST.get("Confirm Password")
    address = request.POST.get("Address")
    resp = {}

    # checking that all fields are available.
    if fname and lname and email and mobile and password and cnf_password and address:
        # check that the mobile number is only 10 digits.
        if len(mobile) == 10:
            # check that the password and confirm password are same.
            # password validation succeed.
            if password == cnf_password:
                respdata = data_insert(fname, lname, email, mobile, password, address)

                # if it returns value then will show success.
                if respdata:
                    resp['status'] = 'Success'
                    resp['status_code'] = '200'
                    resp['message'] = 'User is registered Successfully.'
                # else returning any value then the show will fail.
                else:
                    resp['status'] = 'Failed'
                    resp['status_code'] = '400'
                    resp['message'] = 'Unable to register user, Please try again.'
            # password validation failed.
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Password and Confirm Password should be same.'
        # mobile number validation failed.
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Mobile number should be 10 digits.'
    # if any field is missing.
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'All fields are mandatory.'

    return HttpResponse(json.dumps(resp), content_type = "application/json")