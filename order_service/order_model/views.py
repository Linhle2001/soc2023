# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Order
# Create your views here.
### This function is created for getting the payment. 
def data_insert(uid, shipid, product_id, product_name, quantity, price):
    order_data = Order(user_id = uid, ship_id = shipid, product_id = product_id, product_name = product_name, quantity = quantity, price = price)
    order_data.save()
    return 1
@csrf_exempt
def add_to_order(request):
    uname = request.POST.get("User Name")
    product_id = request.POST.get("Product Id")
    
    url = 'http://127.0.0.1:7000/getcartbyusernameandproid'+uname+'/'+product_id
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    url2 = 'http://127.0.0.1:5000/shipment_status/index'
    headers = {'Content-Type': 'application/json'}
    response2 = requests.post(url, headers=headers, data=uname.json())
    if response.status_code == 200 and response2.status_code==200:
        order = response.json().get('data')
        product_name = order[0].get("product_name")
        product_category = order[0].get("product_category")
        price = order[0].get("totalprice")
        product_size = order[0].get("product_size")
        quantity = order[0].get('count')
        ship = response2.json().get('data')
        shipid = ship[0].get('ship_id')
        respdata = data_insert(uname, shipid, product_id, product_name,quantity, price)
        print(order)
    else:
        print('Error:', response.status_code)
    resp = {}
    if product_id and uname:
    
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
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'All fields are mandatory.'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')