from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import json
import requests
from django.views.decorators.csrf import csrf_exempt
from .models import Cart
# Create your views here.
### This function is created for getting the payment. 
def data_insert(product_id, username, product_category, product_name, product_size, quantity, price):
    cart_data = Cart(product_id = product_id,username = username, product_category = product_category, product_name = product_name, product_size = product_size, count = quantity, totalprice = price)
    cart_data.save()
    
    return 1
from django.urls import reverse

def get_product_url(product_id):
    return reverse('product_service', args=[product_id])
@csrf_exempt
def add_to_cart(request):
    product_id = request.POST.get('product_id')
    customer_name = request.POST.get('customer_name')
    product_count = request.POST.get('count')
    product_size = request.POST.get('size')
    url = 'http://127.0.0.1:8000/shoes/getshoes'+product_id
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        product = response.json().get('data')
        p_id = product[0].get("product_id")
        product_name = product[0].get("product_name")
        product_category = product[0].get("product_category")
        price = str(float(product[0].get("price"))* float(product_count))
        respdata = data_insert(p_id, customer_name, product_category, product_name,product_size, product_count, price)
        print(product)
    else:
        print('Error:', response.status_code)
    
    # val1 = json.loads(response.content.decode('utf-8'))
    # url = 'http://127.0.0.1:8000/userinfo/'
    # data = customer_name
    # headers = {'Content-Type': 'application/json'}
    # response = requests.post(url,data = data, headers=headers)
    # val2 = json.loads(response.content.decode('utf-8'))
   
    resp = {}
    if product_id and customer_name:
   
    ### If it returns value then will show success.
        if response.status_code==200:
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
@csrf_exempt
def getcartbyusernameandproid(request, uname, proid):
    data=[]
    resp ={}
    product_data = Cart.objects.filter(username = uname, product_id = proid)
    for tbl_value in product_data.values():
        data.append(tbl_value)
    # If data is available then it returns the data.
    if data:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = data 
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Data is not available.'
    # return JsonResponse(product_data)
    return HttpResponse(json.dumps(resp), content_type = 'application/json')
