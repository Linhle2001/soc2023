from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from payment.models import payment_status as paystat
from shipment_update.views import shipment_details_update as ship_update
### This function is for fetching the user data.
def get_transaction_details(uname):
    user = paystat.objects.filter(username = uname)
    for data in user.values():
        return data
### This function is used for storing the data.
def store_data(uname, prodid, price, quantity, mode_of_payment, mobile):
    user_data = paystat(username = uname, product_id = prodid, price = 
    price, quantity = quantity, mode_of_payment = mode_of_payment, mobile = 
    mobile, status = "Success")
    user_data.save()
    return 1
### This function is created for getting the payment. 
import requests
@csrf_exempt
def get_payment(request):
    uname = request.POST.get("User Name")
    prodid = request.POST.get("Product id")
    mode_of_payment = request.POST.get("Mode of Payment")
    url = 'http://127.0.0.1:7000/getcartbyusernameandproid'+uname+'/'+prodid
    headers = {'Content-Type': 'application/json'}
    response1 = requests.get(url, headers=headers)
    url2 = 'http://127.0.0.1:8000/userinfo/'
    headers = {'Content-Type': 'application/json'}
    response2 = requests.post(url2, headers=headers, data=uname)
    resp = {}
    if response1.status_code == 200 and response2.status_code==200:
        cart = response1.json().get('data')
        product_name = cart[0].get("product_name")
        product_size = cart[0].get("product_size")
        price = cart[0].get("totalprice")
        quantity = cart[0].get('count')
        user = response2.json().get('data')
        phone = user[0].get('mobile')
        
        respdata = store_data(uname, prodid, price, quantity, mode_of_payment, phone)
        print(cart)
    else:
        print('Error:', response1.status_code)
    
    
        if respdata:
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Transaction is completed.'
        ### If it is returning null value then it will show failed.
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Transaction is failed, Please try again.'
        ### If any mandatory field is missing then it will be through a failed message.
    
### This function is created for getting the username and password. 
@csrf_exempt
def user_transaction_info(request):
    resp = {}
    # uname = request.POST.get("User Name")
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            val1 = json.loads(request.body)
            uname = val1.get('User Name')
            
            if uname:
            ## Calling the getting the user info.
                respdata = get_transaction_details(uname)
                if respdata:
                    resp['status'] = 'Success'
                    resp['status_code'] = '200'
                    resp['data'] = respdata
                ### If a user is not found then it give failed as response.
                else:
                    resp['status'] = 'Failed'
                    resp['status_code'] = '400'
                    resp['message'] = 'User Not Found.'
                ### The field value is missing.
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
