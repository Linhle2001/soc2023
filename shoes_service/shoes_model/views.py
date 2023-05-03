from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from shoes_model.models import Shoes
@csrf_exempt
def getshoesbyname(request, name):
    data=[]
    resp ={}
    product_data = Shoes.objects.filter(product_name = name)
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
@csrf_exempt
def getshoesbycategory(request, category):
    data=[]
    resp ={}
    product_data = Shoes.objects.filter(product_category = category)
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
@csrf_exempt
def getallshose(request):
    data = []
    resp = {}
    # This will fetch the data from the database.
    prodata = Shoes.objects.all()
    for tbl_value in prodata.values():
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
    
    return HttpResponse(json.dumps(resp), content_type = 'application/json')
from django.http import JsonResponse
@csrf_exempt
def getshoes(request, id):
    data=[]
    resp ={}
    product_data = Shoes.objects.filter(product_id = id)
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
@csrf_exempt
def newshoes(request):
    data=[]
    resp ={}
    product_id = request.POST.get("id")
    product_category = request.POST.get("category")
    product_name = request.POST.get("name")
    availability = request.POST.get("availability")
    price = request.POST.get("price")
    image = request.POST.get("image")
    shoes = Shoes(product_id, product_category, product_name, availability, price, image)
    shoes.save()
    data.append(shoes)
    if data:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['message'] = 'Add Shoes Success!' 
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Invailid!'

    return HttpResponse(json.dumps(resp), content_type = 'application/json')